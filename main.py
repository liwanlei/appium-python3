# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
'''主运行文件'''
from untils.pyreport_excel import create
import  unittest,random,datetime
from untils.log import LOG
from  untils.makecase import makecasefile
from multiprocessing import Pool
from  testcase.regcasetest import regtest
from  untils.Parmeris import Parmer
from untils.AppiumServer import AppiumServer
from  untils.BaseApk import getPhoneInfo,AndroidDebugBridge
import os
l_devices=[]
def runnerPool(getDevices):
    devices_Pool = []
    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        print("=====runnerPool=========")
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["udid"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["appPackage"] = 'com.aixuetang.online'
        _initApp["appActivity"] ='com.aixuetang.mobile.activities.HomeActivity'
        _pool.append(_initApp)
        devices_Pool.append(_initApp)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()
def runnerCaseApp(devices):
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parmer.parametrize(regtest,param=devices))
    unittest.TextTestRunner(verbosity=2).run(test_suit)
if __name__=="__main__":
    LOG.info("测试开始执行")
    start_time=datetime.datetime.now()
    devicess = AndroidDebugBridge().attached_devices()
    makecasefile('reg','reg','reg')
    path=os.getcwd()
    filenm=path+'//testreport//'+'result.xls'
    if len(devicess) > 0:
        for dev in devicess:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4562, 4575))
            l_devices.append(app)
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        try:
            appium_server.stop_server(l_devices)
        except:
            pass
        end_time=datetime.datetime.now()
        hour=end_time-start_time
        create(filename=filenm,devices_list=devicess,Test_version='2.0.1',testtime=str(hour))
        LOG.info("测试执行完毕，耗时：%s"%hour)
    else:
        print("没有可用的安卓设备")