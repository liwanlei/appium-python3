""" 
@author: lileilei
@file: beijing.py 
@time: 2018/4/19 10:32 
"""
import  os
from untils.log import  LOG
path=os.getcwd()
def  readheader():
    path_new=path+'//template//case.txt'
    return open(path_new,encoding='utf-8').read()
def readerconet():
    path_new = path + '//template//content.txt'
    conet = open(path_new, encoding='utf-8').read()
    return conet
def  makecasefile(casename,desc,funtionname):
    LOG.info("开始生成测试用例文件")
    filepath=path+'//testcase//'+casename+'casetest.py'
    if not os.path.exists(filepath):
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(readheader().format(casename, casename))
            file.write(readerconet().format(funtionname, desc))
    else:
        pass