# encoding: utf-8  
""" 
@author: lileilei 
@file: recording_txt.py 
@time: 2018/1/20 13:01 
"""
import  os,time
from untils.log import LOG,logger
path=os.getcwd()
now = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
recording=path+'\\testreport\\%s.txt'%now
def write_recording(cpu,neicun,send,resever,sum_liulang):
    try:
        with open(recording,'a',encoding='utf-8') as f:
            m='cpu:%s,内存：%s，发送流量:%s,接受流量：%s，总计：%s'%(cpu,neicun,send,resever,sum_liulang)
            f.write(m+'\n')
            f.close()
    except Exception as e:
        LOG.info('写入性能数据失败！失败原因：%s'%e)