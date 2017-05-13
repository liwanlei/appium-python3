# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: repPorT.py
@time: 2017/4/27 17:08
"""
from public import HTMLTestRunner
import unittest,time
from case import  logintest,registertest
def report(path):
    test_suit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(path,pattern='*test.py',top_level_dir=None)
    for test in discover:
        for test_case in test:
            test_suit.addTest(test_case)
    # now = time.strftime('%Y-%m%d', time.localtime(time.time()))
    report_dir = r'xueshang.html'
    re_open=open(report_dir,'wb')
    renner=HTMLTestRunner.HTMLTestRunner(stream=re_open,title=u'学生端测试',description=u'测试结果')
    renner.run(test_suit)
if __name__=="__main__":
    report(r'..\case')
    from report.email_send import create_report_sendemali
    create_report_sendemali('leileili126@163.com','liwanlei930423','952943386@qq.com')

	