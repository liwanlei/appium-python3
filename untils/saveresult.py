'''
@author: lileilei
@file: saveresult.py
@time: 2018/9/21 15:59
'''
import os,time
from untils.log import logger,LOG
path = os.getcwd()
now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
recording = path + '/testreport/%s.txt' % now
'''记录测试结果'''
@logger('保存测试结果')
def save_result(data):
    if os.path.exists(recording) is True:
        with open(recording,'a',encoding='utf-8') as f:
            f.write(data+'\n')
            f.close()
    else:
        f= open(recording,'a')
        f.write(data+'\n')
        f.close()
    LOG.info('记录测试结果完毕')
@logger('解析测试结果')
def parse_result(devices):
    with open(recording,'r+',encoding='utf-8') as f:
        reslt=f.readlines()
    list_result=[]
    for j in reslt:
        if devices in j:
            list_result.append({'devices':devices,"result":j.split('&')[1],'canshu':j.split('&')[2]})
    passnum=0
    failnum=0
    for i in list_result:
        if i['result']=='pass':
            passnum+=1
        else:
            failnum+=1
    LOG.info('解析设备测试结果完毕')
    return  passnum,failnum, list_result
