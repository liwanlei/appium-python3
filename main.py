# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
from testsuite.repPorT import report
import  os
if __name__=="__main__":
    basepth=os.getcwd()
    path=basepth+'\\testcase'
    report(casepath=path)
