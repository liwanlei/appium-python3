# encoding: utf-8
'''
@author: lileilei
@file: register.py
@time: 2017/4/26 21:09
'''
import yaml,unittest,time
from log.log_case import Logger
from public.zhuce_pub import Regust
from appium import webdriver
class Registe(unittest.TestCase):
    def __init__(self):
        pass
    @classmethod
    def setUpClass(cls):
        cls.dis_app = {}
        cls.dis_app['platformName'] = 'Android'
        cls.dis_app['platformVersion'] = '5.0.2'
        cls.dis_app['deviceName'] = 'emulator-5554'
        cls.dis_app['appPackage'] = 'com.aixuetang.online'
        cls.dis_app['appActivity'] = 'com.aixuetang.mobile.activities.HomeActivity'
        cls.deriver = webdriver.Remote('http://localhost:4723/wd/hub', cls.dis_app)
    def testreg_1(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.deriver.quit()