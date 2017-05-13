# -*- coding: utf-8 -*-
# @Time    : 2017/4/25 12:49
# @Author  : leizi
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from appium import  webdriver
from py_app import deriver_fengzhuang
import time
from selenium.webdriver.support.ui import  WebDriverWait
dis_app={}
dis_app['platformName']='Android'
dis_app['platformVersion']='4.4.2'
dis_app['deviceName']='127.0.0.1:62001'
dis_app['appPackage']='com.aixuetang.online'
dis_app['unicodeKeyboard']=True
dis_app['resetKeyboard']=True
dis_app['appActivity']='com.aixuetang.mobile.activities.HomeActivity'
deriver=webdriver.Remote('http://localhost:4723/wd/hub',dis_app)
time.sleep(10)
try:
    print('chenggong')
    me=deriver_fengzhuang(deriver)
    print('diaoyong')
    hr=me.find_elemens(fangfa='id',lujing='com.aixuetang.online:id/fixed_bottom_navigation_title')
    hr[2].click()
    print('111')
    if me.find_ele('id','com.aixuetang.online:id/toolbar_title').text =='个人中心':
        print('进入个人中心成功')
        me.find_ele('id','com.aixuetang.online:id/login').click()
        if me.find_ele('id','com.aixuetang.online:id/toolbar_title').text=='登录':
            print('进入登录界面')
            username=me.find_ele('id','com.aixuetang.online:id/et_username')
            username.clear()
            username.send_keys('15964636199')
            username_passwored=me.find_ele('id','com.aixuetang.online:id/et_password')
            username_passwored.clear()
            time.sleep(1)
            username_passwored.send_keys('li930423')
            me.find_ele('id','com.aixuetang.online:id/tv_login').click()
            time.sleep(2)
            print('yijingdenglu')
            # if deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip'):
            #     print('fail! resion:%s'%(deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip').text))
            if  me.find_ele('id','com.aixuetang.online:id/user_vip'):
                print('sucess')
                me.find_ele('id','com.aixuetang.online:id/user_setting').click()
                me.find_ele('id','com.aixuetang.online:id/tv_logout').click()
                print('1')
            else:
                print('fail')
        else:
            print('进入失败，请确定定位方式是否正确')
    else:
        print('进入个人中心失败')
        me.kill()
except Exception as e:
    print(e)
    print('启动失败')
    me.kill()
