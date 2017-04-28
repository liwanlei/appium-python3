# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: login_pub.py
@time: 2017/4/27 9:03
"""
from appium import  webdriver
import yaml,time
class Login:
    def __init__(self,deriver):
        self.deriver=deriver
        self.file=open(r'C:\Users\Administrator\Desktop\xuesheng\data\data_dingwei.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.herenzhongxin=self.data['denglu']['weizhilan_id']
        self.logi=self.data['denglu']['denglu_id']
        self.username=self.data['denglu']['username_id']
        self.password=self.data['denglu']['password_id']
        self.log_btn=self.data['denglu']['login_btn_id']
        self.login_fail=self.data['denglu']['denglu_fail_id']
        self.login_sucess=self.data['denglu']['denglu_sucesss_id']
    def login(self,suc,name,password):
        try:
            time.sleep(6)
            self.deriver.find_elements_by_id(self.herenzhongxin)[2].click()
            time.sleep(6)
            self.deriver.find_element_by_id(self.logi).click()
            print('2')
            time.sleep(1)
            usernam=self.deriver.find_element_by_id(self.username)
            usernam.clear()
            usernam.send_keys(name)
            passwor=self.deriver.find_element_by_id(self.password)
            passwor.clear()
            passwor.send_keys(password)
            self.deriver.find_element_by_id(self.log_btn).click()
            if suc == 1:
                self.login_fai=self.deriver.find_element_by_id(self.login_fail).text
                return self.login_fai
            if suc==0:
                self.login_suc=self.deriver.find_element_by_id(self.login_sucess).text
                return self.login_suc
        except Exception as e:
            print(e)
        finally:
            self.deriver.quit()
if __name__ =='__main__':
    Login(deriver=webdriver)