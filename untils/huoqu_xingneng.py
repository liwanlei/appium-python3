# -*- coding: utf-8 -*-
# @Date    : 2017-06-12
# @Author  : lileilei 
import os,time,platform,time
from untils.log import logger,LOG
import  platform,subprocess,os
def getsystemsta():#获取系统的名称，使用对应的指令
	system=platform.system()
	if system=='Windows':
		find_manage='findstr'
	else:
		find_manage='grep'
	return  find_manage
find=getsystemsta()
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| %s %s'%(find,packagename)
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
def getnencun(packagename):#Total 的实际使用过物理内存
	cpu = 'adb shell top -n 1| %s %s' % (find, packagename)
	re_cpu=os.popen(cpu).read().split()[6]
	re_cpu_m=str(round(int(re_cpu[:-1])/1024))+'M'
	return re_cpu_m

