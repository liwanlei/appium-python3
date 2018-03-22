# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: login_pub.py
@time: 2017/4/27 9:03
"""
'''
登录测试
'''
import yaml,time,os
from untils.log import LOG
from untils.huoqu_xingneng import getnencun,caijicpu
from untils.recording_txt import write_recording
from config.config import TestappPackage
class Login:
    def __init__(self,deriver):
        self.deriver=deriver
        LOG.info('获取元素的定位的信息')
        patth=os.getcwd()
        self.file=open(patth+'\\data\\data_dingwei.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.herenzhongxin=self.data['denglu']['weizhilan_id']
        self.logi=self.data['denglu']['denglu_id']
        self.username=self.data['denglu']['username_id']
        self.password=self.data['denglu']['password_id']
        self.log_btn=self.data['denglu']['login_btn_id']
        self.login_fail=self.data['denglu']['denglu_fail_id']
        self.login_sucess=self.data['denglu']['denglu_sucesss_id']
        LOG.info('元素定位信息加载成功！！')
    def login(self,suc,name,password):
        self.deriver.find_elements_by_id(self.herenzhongxin)[2].click()
        self.deriver.find_element_by_id(self.logi).click()
        LOG.info('进入登陆界面！！')
        userna=self.deriver.find_element_by_id(self.username)
        userna.clear()
        userna.send_keys(name)
        passwor=self.deriver.find_element_by_id(self.password)
        passwor.clear()
        passwor.send_keys(password)
        path=os.getcwd()
        pathw = path + '\\testpang\\%s.jpg' %(str(time.time())[:10])
        LOG.info('登陆参数输入完毕')
        self.deriver.find_element_by_id(self.log_btn).click()
        neicun = getnencun(TestappPackage)
        cpu = caijicpu(TestappPackage)
        write_recording(cpu=cpu,neicun=neicun)
        LOG.info('登录占内存:%s,cpu：%s'%(neicun,cpu))
        self.deriver.get_screenshot_as_file(pathw)
        time.sleep(5)
        if suc =='1' or suc==1:
            self.login_fai=self.deriver.find_element_by_id(self.login_fail).text
            return self.login_fai
        if suc=='0' or suc==0:
            self.login_suc=self.deriver.find_element_by_id(self.login_sucess).text
            return self.login_suc
