# encoding: utf-8
'''
@author: lileilei
@file: regtest.py
@time: 2017/4/26 21:09
'''
'''登录测试用例
才用ddt数据驱动'''
from appium import webdriver
import unittest,ddt,os,time
from untils.log import LOG
from untils.disapp import make_dis
from untils.gettestdata import huoqu_test
from funtions.regpub import RegFuntion
from untils.huoqu_xingneng import caijicpu,getnencun
from untils.recording_txt import write_recording
from config.config import TestappPackage
path=os.getcwd()
testcasedata=path+'\\data\\testcase_data.xlsx'
data_test=huoqu_test(testcasedata,index=1)
@ddt.ddt
class Regpuliblisdt(unittest.TestCase):
    def setUp(self):
        self.dis_app = make_dis()
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        LOG.info('reg测试用例开始执行')
    @ddt.data(*data_test)
    def test_reg(self,data_test):
        regfun=RegFuntion(deriver=self.deriver)
        self.assertuen=regfun.reg(**data_test)
        cpu=caijicpu(TestappPackage)
        neicun=getnencun(TestappPackage)
        write_recording(cpu=cpu,neicun=neicun)
        self.assertEqual(data_test['assert'],self.assertuen,msg='fail resons:%s !=%s'%(data_test['assert'],self.assertuen))
    def tearDown(self):
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(15)
        self.deriver.quit()