""" 
@author: lileilei
@file: beijing.py 
@time: 2018/4/19 10:32 
"""
import os
from untils.log import LOG
from  config.config import Test_mobile_type
path = os.getcwd()


def readheader():
    pathone=os.path.join(path,"template")
    path_new = pathone + 'case.txt'
    return open(path_new, encoding='utf-8').read()


def readerconet():
    pathone = os.path.join(path, "template")
    path_new = pathone + 'content.txt'
    conet = open(path_new, encoding='utf-8').read()
    return conet

def readiosheader():
    pathone=os.path.join(path,"template")
    path_new = pathone + 'ioscase.txt'
    return open(path_new, encoding='utf-8').read()


def readeriosconet():
    pathone = os.path.join(path, "template")
    path_new = pathone + 'ioscontent.txt'
    conet = open(path_new, encoding='utf-8').read()
    return conet


def makecasefile(casename, desc, funtionname):
    LOG.info("开始生成测试用例文件")
    pathone = os.path.join(path, "testcase")
    filepath = pathone  + '{}casetest.py'.format(casename)
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            if Test_mobile_type=="Android":
                file.write(readheader().format(casename, casename))
                file.write(readerconet().format(funtionname, desc))
            else:
                file.write(readiosheader().format(casename, casename))
                file.write(readeriosconet().format(funtionname, desc))