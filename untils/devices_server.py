# encoding: utf-8
'''
@author: lileilei
@file: devices_server.py
@time: 2017/5/1 15:45
'''
import os,requests
from multiprocessing import Pool
from time import  sleep
import time
from config.config import TestappActivity,TestappPackage
class Initdevices:
    def __init__(self):
        self.get_android='adb devices'
        self.get_ios='instruments -s devices'
    def get_devices(self):
        value=os.popen(self.get_android)
        devices=[]
        for v in value.readlines():
            android={}
            s_value=str(v).replace("\n","").replace("\t","")
            if s_value.rfind('device') !=  -1 and (not s_value.startswith('List')) and s_value !='':
                android['deviceName']=s_value[:s_value.find('device')].strip()
                android['platformName'] = 'Android'
                android['package'] =TestappPackage
                android['activity'] = TestappActivity
                devices.append(android)
        # value = os.popen(self.GET_IOS)
        #
        # for v in value.readlines():
        #     iOS = {}
        #
        #     s_value = str(v).replace("\n", "").replace("\t", "").replace(" ", "")
        #
        #     if v.rfind('Simulator') != -1:
        #         continue
        #     if v.rfind("(") == -1:
        #         continue
        #
        #     iOS['platformName'] = 'iOS'
        #     iOS['platformVersion'] = re.compile(r'\((.*)\)').findall(s_value)[0]
        #     iOS['deviceName'] = re.compile(r'(.*)\(').findall(s_value)[0]
        #     iOS['udid'] = re.compile(r'\[(.*?)\]').findall(s_value)[0]
        #     iOS['bundleId'] = 'xxxx'
        #
        #     devices.append(iOS)

        return devices
def is_using(port):
    cmd='netstat -an | grep %s'%port
    if os.popen(cmd).realines():
        return  True
    else:
        return False
def get_port(count):
    port=3456
    port_list=[]
    while True:
        if len(port_list) ==count:
            break
        if not is_using(port) and (port in port_list):
            port_list.append(port)
        else:
            port+=1
    return port_list
class appiumServer():
    def __init__(self,devices):
        self.devices=devices
        self.count=len(devices)
        self.url='http://127.0.0.1:%s/wd/hub/'
        self.takkill= 'taskkill /PID %d /F'
        self._pids = []
    def kill_appium_server(self):
        for pid in self._pids:
            os.popen(self.takkill % pid)
    def start_server(self):
        pool = Pool(processes=len(self.devices))
        for run in self.devices:
            pool.apply_async(self._run_server, args=(run,))
        pool.close()
        pool.join()
        for run in self.devices:
            while not self.is_running(run.get_port()):
                print('wait appium server all ready...')
                time.sleep(1)
        print('appium server all ready')
        '''testlog rizhi'''
        for run in self.devices:
            file = str(run.get_path() + '\\' + self._file) % run.get_port()
            with open(file, 'r') as f:
                line = f.readline()
                start = line.find('pid:')
                end = line[start:].find(' ')

                pid = line[start:][4:end]
                self._pids.append(int(pid))

    def run_server(self,device,port):
        while not  self.is_running(port):
            sleep(1)
        server_url = {
            'hostname': "127.0.0.1",
            'port': port,
        }
        return  server_url
    def is_running(self, port):
        url = self.url % port
        response = None
        try:
            response = requests.get(url, timeout=0.01)
            if str(response.status_code).startswith('2'):
                # data = json.loads((response.content).decode("utf-8"))
                # if data.get("staus") == 0:
                return True
            return False
        except requests.exceptions.ConnectionError:
            return False
        except requests.exceptions.ReadTimeout:
            return False
        finally:
            if response:
                response.close()
    def _run_server(self, run):
        port = run.get_port()
        cmd = str(self._cmd + ' > ' + run.get_path() + '\\' + self._file) % (port, port)
        os.system(cmd)