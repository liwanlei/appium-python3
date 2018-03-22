# encoding: utf-8  
""" 
@author: lileilei 
@file: regtest.py 
@time: 2018/1/20 10:31 
"""
'''注册测试用例，采取ddt数据驱动，数据来自于Excel写的测试文档'''
import unittest,time,ddt,os
from untils.log import LOG
from business.zhuce_pub import Regust
from appium import webdriver
from untils.disapp import make_dis
from untils.gettestdata import huoqu_test
path=os.getcwd()
testcasedata=path+'\\data\\testcase_data.xlsx'
data_test=huoqu_test(testcasedata,index=1)
@ddt.ddt
class Registe(unittest.TestCase):
    def setUp(self):
        '''初始化测试环境'''
        self.dis_app =make_dis()
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        self.res=Regust(self.deriver)
        LOG.info('register测试用例环境初始化完毕,开始执行测试用例')
    @ddt.data(*data_test)
    def testreg(self,data_test):
        self.user=data_test['username']
        self.password=data_test['password']
        self.yanzheng=data_test['yanzhengma']
        self.suc=data_test['suc']
        self.asserts=data_test['assert']
        self.asser_return=self.res.register1(self.suc,self.user,self.password,self.yanzheng)
        LOG.info(('测试用例：%s,输入参数:name:%s,pwd:%s,yanzhengma:%s suc:%s,assert:%s' % (data_test['id'],self.user, self.password, self.yanzheng,self.suc, self.asserts)))
        time.sleep(1)
        self.assertEqual(self.asser_return,self.asserts,msg='fail resons:%s !=%s'%(self.asser_return,self.asserts))
    def tearDown(self):
        LOG.info('清空测试环境操作中')
        self.deriver.quit()