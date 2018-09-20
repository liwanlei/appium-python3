# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
'''主运行文件'''
from testsuite.repPorT import report
import  os,unittest,random
from untils.log import LOG
from multiprocessing import Pool
from untils.AppiumServer import AppiumServer
from  untils.BaseApk import ApkInfo,getPhoneInfo,AndroidDebugBridge
def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        print("=====runnerPool=========")
        print(getDevices)
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["udid"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]
        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()
        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()
def runnerCaseApp(devices):
    basepth = os.getcwd()
    path = basepth + '\\testcase'
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(path, pattern='*test.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            suite.addTest(test_case)
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
if __name__=="__main__":
    # devicess = AndroidDebugBridge().attached_devices()
    # if len(devicess) > 0:
    #     l_devices = []
    #     for dev in devicess:
    #         app = {}
    #         app["devices"] = dev
    #         app["port"] = str(random.randint(4700, 4900))
    #         app["bport"] = str(random.randint(4700, 4900))
    #         app["systemPort"] = str(random.randint(4700, 4900))
    #         l_devices.append(app)
    #
    #     appium_server = AppiumServer(l_devices)
    #     appium_server.start_server()
    #     runnerPool(l_devices)
    #     appium_server.stop_server(l_devices)
    #     # 中断logcat
    #     # kill_adb()
    #
    # else:
    #     print("没有可用的安卓设备")
    LOG.info('UI自动化相关测试开始执行')
    basepth=os.getcwd()
    path=basepth+'\\testcase'
    report(casepath=path)
    LOG.info('UI自动化相关测试执行完毕！')