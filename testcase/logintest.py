# encoding: utf-8
'''
@author: lileilei
@file: logintest.py
@time: 2017/4/26 21:09
'''
'''登录测试用例
才用ddt数据驱动'''
from appium import webdriver
import unittest,ddt,os,time
from untils.log import LOG
from untils.disapp import make_dis
from untils.gettestdata import huoqu_test
from business.login_pub import Login
path=os.getcwd()
testcasedata=path+'\\data\\testcase_data.xlsx'
path_yongli=path+'\\data\\dingwei\\reg.yaml'
data_test=huoqu_test(testcasedata,index=0)
@ddt.ddt
class Logintest(unittest.TestCase):
    def setUp(self):
        self.dis_app = make_dis()
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        self.logs=Login(self.deriver,path)
        LOG.info('login测试用例开始执行')
    @ddt.data(*data_test)
    def test_login(self,data_test):
        login=Login(deriver=self.deriver,path=path_yongli)
        self.assertuen=login.login(**data_test)
        self.assertEqual(self.assert_v,self.assertuen,msg='fail resons:%s !=%s'%(self.assert_v,self.assertuen))
    def tearDown(self):
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(15)
        self.deriver.quit()