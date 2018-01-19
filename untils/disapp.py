""" 
@author: lileilei
@file: disapp.py 
@time: 2018/1/19 11:10 
"""
from  config.config import *
def make_dis():
    dis_app={}
    dis_app['platformName'] = Testplatform
    dis_app['platformVersion'] = TestplatformVersion
    dis_app['deviceName'] = Testdevicesname
    dis_app['appPackage'] = TestappPackage
    dis_app['appActivity'] =TestappActivity
    dis_app['androidDeviceReadyTimeout'] =TestandroidDeviceReadyTimeout
    dis_app['unicodeKeyboard'] = TestunicodeKeyboard
    dis_app['resetKeyboard'] =TestresetKeyboard
    return  dis_app