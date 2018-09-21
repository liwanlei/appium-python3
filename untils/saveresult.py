'''
@author: lileilei
@file: saveresult.py
@time: 2018/9/21 15:59
'''
import os
'''记录测试结果'''
def save_result(data):
    file=os.getcwd()
    file_path=file+'//result.txt'
    if os.path.exists(file_path) is True:
        with open(file,'a+',encoding='utf-8') as f:
            f.writelines(data+'\n')
    else:
        f= open(file_path,'a+')
        f.write(data+'\n')
        f.close()
