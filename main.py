# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
'''主运行文件'''
from untils.pyreport_excel import create
import unittest, random, datetime
from untils.log import LOG, logger
from untils.makecase import makecasefile
from multiprocessing import Pool
from testcase.regcasetest import regtest
from untils.Parmeris import Parmer
from untils.AppiumServer import AppiumServer
from untils.BaseApk import getPhoneInfo, AndroidDebugBridge
import os

l_devices = []


@logger('生成设备配置链接的进程池')
def runnerPool(getDevices):
    '''
       根据链接的设备生成不同的dict
       然后放到设备的list里面
       设备list的长度产生进程池大小
    '''
    devices_Pool = []
    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["udid"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["appPackage"] = 'com.aixuetang.online'
        _initApp["appActivity"] = 'com.aixuetang.mobile.activities.HomeActivity'
        _pool.append(_initApp)
        devices_Pool.append(_initApp)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


@logger('组织测试用例')
def runnerCaseApp(devices):
    '''利用unittest的testsuite来组织测试用例'''
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parmer.parametrize(regtest, param=devices))  # 扩展的其他的测试用例均这样添加
    unittest.TextTestRunner(verbosity=2).run(test_suit)


if __name__ == "__main__":
    LOG.info("测试开始执行")
    start_time = datetime.datetime.now()
    devicess = AndroidDebugBridge().attached_devices()
    makecasefile('reg', 'reg', 'reg')  # 没有的时候才会生成，一般都会有这个文件
    path = os.getcwd()
    filenm = path + '//testreport//' + 'result.xls'
    if len(devicess) > 0:
        for dev in devicess:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4593, 4598))
            l_devices.append(app)
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()  # 启动服务
        runnerPool(l_devices)
        try:
            appium_server.stop_server(devicess)
        except Exception as e:
            LOG.info("关闭服务失败，原因：%s" % e)
        end_time = datetime.datetime.now()
        hour = end_time - start_time
        create(filename=filenm, devices_list=devicess, Test_version='2.0.1', testtime=str(hour))
        LOG.info("测试执行完毕，耗时：%s" % hour)
    else:
        LOG.info("没有可用的安卓设备")
        print("没有可用的安卓设备")
