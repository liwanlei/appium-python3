'''
@author: lileilei
@file: AppiumServer.py
@time: 2018/9/20 14:37
'''
import os,urllib.request
from multiprocessing import Process
import threading,time,platform,subprocess
from untils.log import LOG,logger
'''启动appium服务'''
class RunServer(threading.Thread):#启动服务的线程
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)
class AppiumServer(object):
    def __init__(self,kwargs):
        self.kwargs=kwargs
    def run(self,url):
        time.sleep(10)
        response = urllib.request.urlopen(url, timeout=5)
        if str(response.getcode()).startswith("2"):
            return True
    def start_server(self):#开启服务
        for i in range(0, len(self.kwargs)):
            cmd = "appium --session-override  -p %s  -U %s" % (
                self.kwargs[i]["port"],  self.kwargs[i]["devices"])
            if platform.system() == "Windows":  # windows下启动server
                t1 = RunServer(cmd)
                p = Process(target=t1.start())
                p.start()
                while True:
                    time.sleep(4)
                    if self.run("http://127.0.0.1:" + self.kwargs[i]["port"] + "/wd/hub/status"):
                        LOG.info("-------win_server_ 成功--------------")
                        break
            else:
                appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,
                                          close_fds=True)
                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    time.sleep(2)
                    print("---------start_server----------")
                    if 'listener started' in appium_line or 'Error: listen' in appium_line:
                        print("----server启动成功---")
                        break
    def stop_server(devices:list):
        sysstr = platform.system()
        if sysstr == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            for device in devices:
                cmd = "lsof -i :{0}".format(device["port"])
                plist = os.popen(cmd).readlines()
                plisttmp = plist[1].split("    ")
                plists = plisttmp[1].split(" ")
                os.popen("kill -9 {0}".format(plists[0]))