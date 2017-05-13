# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: main.py
@time: 2017/4/27 13:41
"""
from report.repPorT import report
from  report.email_send import create_report_sendemali
if __name__=="__main__":
    report(r'C:\Users\Administrator\Desktop\appium-python3\case')
    create_report_sendemali('leileili126@163.com','liwanlei930423','952943386@qq.com')