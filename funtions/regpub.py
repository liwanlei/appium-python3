# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: regpub.py
@time: 2017/4/27 9:03
"""
'''
注册测试
'''
from untils.log import LOG, logger
from excetfuntion.exectfuntion import Makeappcase
import os


@logger('注册测试')
class RegFuntion:
    def __init__(self, deriver):
        path = os.getcwd()
        path_ = os.path.join(os.path.join(path, 'data'), 'location')
        self.path = path_ + 'reg.yaml'
        self.deriver = deriver
        self.open = Makeappcase(self.deriver, path=self.path)

    def reg(self, **kwargs):
        f = self.open.exce_case(**kwargs)
        if f['code'] == 1:
            LOG.info('无法获取断言')
            return
        else:
            beijing = f['data']
            return beijing
