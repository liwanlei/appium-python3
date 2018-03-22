# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
'''主运行文件'''
from testsuite.repPorT import report
import  os
from untils.log import LOG
if __name__=="__main__":
    LOG.info('UI自动化相关测试开始执行')
    basepth=os.getcwd()
    path=basepth+'\\testcase'
    report(casepath=path)
    LOG.info('UI自动化相关测试执行完毕！')
