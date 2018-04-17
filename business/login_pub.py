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
from untils.log import LOG,logger
from business.exectfuntion import Makeappcase
@logger('登录测试函数')
class Login:
    def __init__(self,deriver,path):
        self.deriver=deriver
        self.path=path
        self.open=Makeappcase(self.deriver,path=self.path)
    def login(self,**kwargs):
        f=self.open.exce_case(**kwargs)
        if f['code']==1:
            LOG.info('无法获取断言')
        else:
            beijing=f['data']
        return beijing