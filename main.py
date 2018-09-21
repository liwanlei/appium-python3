# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
'''主运行文件'''
from testsuite.repPorT import report
import  os,unittest,random,time,datetime
from  untils.BSTestRunner import BSTestRunner
from untils.log import LOG
from  untils.makecase import makecasefile
from multiprocessing import Pool
from  testcase.regcasetest import regtest
from  untils.Parmeris import Parmer
from untils.AppiumServer import AppiumServer
from untils.htmlreport import createHtml
from  untils.BaseApk import getPhoneInfo,AndroidDebugBridge
l_devices=[]
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
        _initApp["appPackage"] = 'com.aixuetang.online'
        _initApp["appActivity"] ='com.aixuetang.mobile.activities.HomeActivity'
        _pool.append(_initApp)
        devices_Pool.append(_initApp)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()
def runnerCaseApp(devices):
    basepth = os.getcwd()
    path = basepth + '\\testcase'
    test_suit = unittest.TestSuite()
    test_suit.addTest(Parmer.parametrize(regtest,param=devices))
    # discover = unittest.defaultTestLoader.discover(path, pattern='*test.py', top_level_dir=None)
    # for test in discover:
    #     for test_case in test:
    #         test_suit.addTest(test_case)
    # unittest.TextTestRunner(verbosity=2).run(test_suit)
    now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    path = os.getcwd()
    report_dir = path + '\\testreport\\%s.html' % now
    re_open = open(report_dir, 'wb')
    runner = BSTestRunner(stream=re_open, title=u'学生端app UI自动化测试', description=u'自动化测试结果')
    runner.run(test_suit)
if __name__=="__main__":
    start_time=datetime.datetime.now()
    devicess = AndroidDebugBridge().attached_devices()
    makecasefile('reg','reg','reg')
    if len(devicess) > 0:
        for dev in devicess:
            app = {}
            app["devices"] = dev
            app["port"] = str(random.randint(4529, 4530))
            l_devices.append(app)
        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        appium_server.stop_server(l_devices)
        # 中断logcat
        # kill_adb()
        end_time=datetime.datetime.now()
        hour=end_time-start_time
    else:
        print("没有可用的安卓设备")
    # LOG.info('UI自动化相关测试开始执行')
    # basepth=os.getcwd()
    # path=basepth+'\\testcase'
    # report(casepath=path)
    # LOG.info('UI自动化相关测试执行完毕！')