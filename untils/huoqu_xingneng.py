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
def liulang(packagename):
	try:
		cmd='adb shell cat /data/system/packages.list | %s %s'%(find,packagename)
		cm=os.popen(cmd).read().split()[1]
		cmd1='adb shell cat /proc/net/xt_qtaguid/stats | %s %s'%(find,cm)
		me1_shou=os.popen(cmd1).read().split()[5]#接受
		me2_shou=os.popen(cmd1).read().split()[7]#上传
		cmd2='adb shell cat /proc/net/xt_qtaguid/stats | %s %s'%(find,cm)
		me1_xia=os.popen(cmd1).read().split()[5]#接受
		me2_xia=os.popen(cmd1).read().split()[7]#上传
		liulang_sum_1=(int(me1_shou)+int(me2_shou))#过程产生流量计算为执行后的流量-执行前的流量，
		liulang_sum_xia=(int(me1_xia)+int(me2_xia))
		liulang_sum=int(liulang_sum_xia)-int(liulang_sum_1)
		me1=int(me1_xia)-int(me1_shou)
		me2=int(me2_xia)-int(me2_shou)
		return me1 ,me2,liulang_sum
	except Exception as e:
		LOG.info('获取流量失败！')
		me1=0
		me2=0
		liulang_sum=0
		return me1,me2,liulang_sum
def caijicpu(packagename):#这里采集的cpu时候可以是执行操作采集 就是-n  -d  刷新间隔
	cpu='adb shell top -n 1| %s %s'%(find,packagename)
	re_cpu=os.popen(cpu).read().split()[2]
	return re_cpu
def getnencun(packagename):#Total 的实际使用过物理内存
	cpu = 'adb shell top -n 1| %s %s' % (find, packagename)
	re_cpu=os.popen(cpu).read().split()[6]
	re_cpu_m=str(round(int(re_cpu[:-1])/1024))+'M'
	return re_cpu_m

