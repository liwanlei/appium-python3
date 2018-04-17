# encoding: utf-8
"""
@author: lileilei
@file: repPorT.py
@time: 2017/4/27 17:08
"""
'''组织测试用例'''
from untils import BSTestRunner
import unittest,time,os
from untils.log import  LOG
def report(casepath):
    test_suit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(casepath,pattern='*test.py',top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)
    now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    path=os.getcwd()
    report_dir = path+'\\testreport\\%s.html'%now
    LOG.info('测试报告路径为：%s'%report_dir)
    re_open=open(report_dir,'wb')
    runner=BSTestRunner.BSTestRunner(stream=re_open,title=u'学生端app UI自动化测试',description=u'自动化测试结果')
    runner.run(test_suit)