# encoding: utf-8
'''
@author: lileilei
@file: logintest.py
@time: 2017/4/26 21:09
'''
from appium import webdriver
import yaml,unittest,time,ddt,os
from business.logout_pub import logout
from business.login_pub import Login
from untils.log import LOG
from untils.disapp import make_dis
from untils.gettestdata import huoqu_test
path=os.getcwd()
testcasedata=path+'\\data\\testcase_data.xlsx'
data_test=huoqu_test(testcasedata)
@ddt.ddt
class Logintest(unittest.TestCase):
    def setUp(self):
        self.dis_app = make_dis()
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        time.sleep(10)
        self.logs=Login(self.deriver)
        LOG.info('测试用例:开始执行')
    @ddt.data(*data_test)
    def test_login(self,data_test):
        self.user=data_test['username']
        self.passw = data_test['password']
        self.suc=data_test['suc']
        self.assert_v=data_test['assert']
        self.assert_return=self.logs.login(suc=self.suc,name=self.user,password=self.passw)
        LOG.info('登录测试，传入参数:用户名：%s，密码：%s,返回结果：%s'%(self.user,self.passw,self.assert_return))
        pathw=path+'\\testpang\%s.pang'%data_test['id']
        self.deriver.get_screenshot_as_file(pathw)
        self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
    def tearDown(self):
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        self.deriver.quit()