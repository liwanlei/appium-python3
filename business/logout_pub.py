# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: logout_pub.py
@time: 2017/4/27 13:07
"""
import yaml
class logout:
    def __init__(self,deriver):
        self.deriver=deriver
        self.file=open(r'..\data\data_dingwei.yaml','r',encoding='utf-8')
        self.data=yaml.load(self.file)
        self.file.close()
        self.shezhi=self.data['logut']['shezhi_id']
        self.logut=self.data['logut']['logut_id']
        self.logut_suc=self.data['logut']['logut_sucess']
        self.logut_fail=self.data['logut']['logut_fail']
    def lohout(self):
            self.deriver.find_element_by_id(self.shezhi).click()
            self.deriver.find_element_by_id(self.logut).click()