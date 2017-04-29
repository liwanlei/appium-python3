# encoding: utf-8
'''
@author: lileilei
@file: logintest.py
@time: 2017/4/26 21:09
'''
from appium import webdriver
import yaml,unittest,time
from public.logout_pub import logout
from log.log_case import Logger
from public.login_pub import Login
class Logintest(unittest.TestCase):
    def setUp(self):
        title='登录测试'
        self.dis_app = {}
        self.dis_app['platformName'] = 'Android'
        self.dis_app['platformVersion'] = '5.1.1'
        self.dis_app['deviceName'] = 'emulator-5554'
        self.dis_app['appPackage'] = 'com.aixuetang.online'
        self.dis_app['appActivity'] = 'com.aixuetang.mobile.activities.HomeActivity'
        self.deriver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_app)
        time.sleep(10)
        self.faile=open(r'C:\Users\Administrator\Desktop\appium-python3\data\data_case.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.faile)
        self.faile.close()
        self.logcan=Logger(title)
        self.data=self.data['login']
        self.logs=Login(self.deriver)
    def test_login_1(self):
        try:
            self.user=self.data['login1']['username']
            self.passw = self.data['login1']['password']
            self.suc=self.data['login1']['suc']
            self.assert_v=self.data['login1']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'login1.pang')
            self.logcan.info_log('input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            print('login1')
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s'%e)
            print('login1 fail,reson:%s'%e)
    def test_login_2(self):
        try:
            self.user=self.data['login2']['username']
            self.passw = self.data['login2']['password']
            self.suc=self.data['login2']['suc']
            self.assert_v=self.data['login2']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login2.pang')
            self.logcan.info_log('input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            print('login1')
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login2 fail,reson:%s'%e)
    def test_login_3(self):
        try:
            self.user=self.data['login3']['username']
            self.passw = self.data['login3']['password']
            self.suc=self.data['login3']['suc']
            self.assert_v=self.data['login3']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login3.pang')
            self.logcan.info_log('input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            print('login1')
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login3 fail,reson:%s'%e)
    def test_login_4(self):
        try:
            self.user=self.data['login4']['username']
            self.passw = self.data['login4']['password']
            self.suc=self.data['login4']['suc']
            self.assert_v=self.data['login4']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login4.pang')
            self.logcan.info_log('input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            print('login1')
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login4 fail,reson:%s'%e)
    def test_login_8(self):
        try:
            self.user=self.data['login8']['username']
            self.passw = self.data['login8']['password']
            self.suc=self.data['login8']['suc']
            self.assert_v=self.data['login8']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login8.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            print('login1')
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login8 fail,reson:%s'%e)
    def test_login_9(self):
        try:
            self.user=self.data['login9']['username']
            self.passw = self.data['login9']['password']
            self.suc=self.data['login9']['suc']
            self.assert_v=self.data['login9']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login9.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login9 fail,reson:%s'%e)
    def test_login_10(self):
        try:
            self.user=self.data['login10']['username']
            self.passw = self.data['login10']['password']
            self.suc=self.data['login10']['suc']
            self.assert_v=self.data['login10']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login710.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login10 fail,reson:%s'%e)
    def test_login_11(self):
        try:
            self.user=self.data['login11']['username']
            self.passw = self.data['login11']['password']
            self.suc=self.data['login11']['suc']
            self.assert_v=self.data['login11']['assert']
            self.assert_return=self.logs.login(self.suc,self.user,self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login11.pang')
            self.logcan.info_log('input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
        except Exception as e:
            self.logcan.error_log(u'失败原因：%s' % e)
            print('login11 fail,reson:%s'%e)

    def test_login_5(self):
        try:
            self.user = self.data['login5']['username']
            self.passw = self.data['login5']['password']
            self.suc = self.data['login5']['suc']
            self.assert_v = self.data['login5']['assert']
            self.assert_return = self.logs.login(self.suc, self.user, self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login5.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,
                             msg='fail resons:%s !=%s' % (self.assert_v, self.assert_return))
            logout.logou(0)
        except Exception as e:
            self.logcan.error_log(e)
            print('login5 fail,reson:%s' % e)

    def test_login_6(self):
        try:
            self.user = self.data['login6']['username']
            self.passw = self.data['login6']['password']
            self.suc = self.data['login6']['suc']
            self.assert_v = self.data['login6']['assert']
            self.assert_return = self.logs.login(self.suc, self.user, self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login6.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,
                             msg='fail resons:%s !=%s' % (self.assert_v, self.assert_return))
            logout.logou(0)
        except Exception as e:
            self.logcan.error_log(e)
            print('login6 fail,reson:%s' % e)

    def test_login_7(self):
        try:
            self.user = self.data['login7']['username']
            self.passw = self.data['login7']['password']
            self.suc = self.data['login7']['suc']
            self.assert_v = self.data['login7']['assert']
            self.assert_return = self.logs.login(self.suc, self.user, self.passw)
            self.deriver.get_screenshot_as_file(r'C:\Users\Administrator\Desktop\appium-python3\jietu\login7.pang')
            self.logcan.info_log(
                'input data:name:%s,pwd:%s, suc:%s,assert:%s' % (self.user, self.passw, self.suc, self.assert_v))
            time.sleep(1)
            self.assertEqual(self.assert_v, self.assert_return,
                             msg='fail resons:%s !=%s' % (self.assert_v, self.assert_return))
            logout.logou(0)
        except Exception as e:
            self.logcan.error_log(e)
            print('login7 fail,reson:%s' % e)
    def tearDown(self):
        self.deriver.close()
        self.deriver.quit()