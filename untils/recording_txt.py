# encoding: utf-8  
""" 
@author: lileilei 
@file: recording_txt.py 
@time: 2018/1/20 13:01 
"""
'''采集的性能测试数据存放在txt文档中'''
import  os,time
from untils.log import LOG,logger
path=os.getcwd()
now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
recording=path+'\\testreport\\%s-xing.txt'%now
@logger('记录当前的cpu占有率，内存')
def write_recording(cpu,neicun,devices):
    try:
        with open(recording,'a',encoding='utf-8') as f:
            m='%s：cpu:%s,内存：%s'%(devices,cpu,neicun)
            f.write(m+'\n')
            f.close()
    except Exception as e:
        LOG.info('写入性能数据失败！失败原因：%s'%e)