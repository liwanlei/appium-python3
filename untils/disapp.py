""" 
@author: lileilei
@file: disapp.py 
@time: 2018/1/19 11:10 
"""
'''
从配置文件获取相关的app测试配置信息
'''
from  config.config import *
from  untils.log import logger
@logger('开始从配置文件中获取测试相关的配置')
def make_dis(Testplatform,TestplatformVersion,Testdevicesname,TestappPackage,TestappActivity):
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