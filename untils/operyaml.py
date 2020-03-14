""" 
@author: lileilei
@file: operyaml.py 
@time: 2018/4/17 12:55 
"""
import yaml
from untils.log import LOG, logger


@logger('解析yaml文件')
def open_da(path):
    try:
        file = open(r'%s' % path, 'r', encoding='utf-8')
        data = yaml.load(file)
        return {'code': 0, 'data': data}
    except Exception as e:
        LOG.info('yaml文档解析失败！原因：%s' % e)
        return {'code': 1, 'data': e}
