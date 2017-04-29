# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: logout_pub.py
@time: 2017/4/27 13:07
"""
from appium import  webdriver
from log.log_case import Logger
import yaml
class logout:
    def __init__(self,deriver):
        self.deriver=deriver
        title='logout'
        self.file=open(r'C:\Users\Administrator\Desktop\appium-python3\data\data_dingwei.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.shezhi=self.data['logut']['shezhi_id']
        self.logut=self.data['logut']['logut_id']
        self.logut_suc=self.data['logut']['logut_sucess']
        self.logut_fail=self.data['logut']['logut_fail']
        self.logs=Logger(title)
    def logou(self,suc):
        try:
            self.deriver.find_element_by_id(self.shezhi).click()
            self.deriver.find_element_by_id(self.logut).click()
            if suc ==1:
                self.text_fail=self.deriver.find_element_by_id(self.logut_fail).text
                return self.text_fail
            if suc==0:
                self.text_suc=self.deriver.find_element_by_id(self.logut_suc).text
                return self.text_suc
        except Exception as e:
            self.logs.error_log(e)
            print(e)
        finally:
            self.deriver.quit()