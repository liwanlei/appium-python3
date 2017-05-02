# encoding: utf-8
'''
@author: lileilei
@file: log_case.py
@time: 2017/4/26 20:50
'''
import  logging,os,time
class Logger():
    def __init__(self,title):
        self.day = time.strftime("%Y%m%d", time.localtime(time.time()))
        self.logger=logging.Logger(title)
        self.logger.setLevel(logging.INFO)
        self.logfile=logging.FileHandler(r'C:\Users\Administrator\Desktop\xuesheng\log\%s.log'%self.day)
        self.logfile.setLevel(logging.INFO)
        self.control=logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)
    def debugInfo(self,message):
        self.logger.debug(message)
    def info_log(self,message):
        self.logger.info(message)
    def ware_log(self,message):
        self.logger.warn(message)
    def error_log(self,message):
        self.logger.error(message)
