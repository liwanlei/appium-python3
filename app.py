# -*- coding: utf-8 -*-
# @Time    : 2017/4/25 12:49
# @Author  : leizi
# @Site    : 
# @File    : app.py
# @Software: PyCharm
from appium import  webdriver
import time
dis_app={}
dis_app['platformName']='Android'
dis_app['platformVersion']='5.0.2'
dis_app['deviceName']='emulator-5554'
dis_app['appPackage']='com.aixuetang.online'
dis_app['appActivity']='com.aixuetang.mobile.activities.HomeActivity'
deriver=webdriver.Remote('http://localhost:4723/wd/hub',dis_app)
time.sleep(10)
try:
    print('chenggong')
    deriver.find_elements_by_id('com.aixuetang.online:id/fixed_bottom_navigation_title')[2].click()
    print('111')
    if deriver.find_element_by_id('com.aixuetang.online:id/toolbar_title').text =='个人中心':
        print('进入个人中心成功')
        deriver.find_element_by_id('com.aixuetang.online:id/login').click()
        if deriver.find_element_by_id('com.aixuetang.online:id/toolbar_title').text=='登录':
            print('进入登录界面')
            # deriver.find_element_by_id('com.aixuetang.online:id/toolbar_menu').click()
            # if deriver.find_element_by_id('com.aixuetang.online:id/toolbar_title').text=='注册':
            #     print('come  zhuce!')
            #     username=deriver.find_element_by_id('com.aixuetang.online:id/et_username')
            #     username.clear()
            #     username.send_keys('15964636199')
            #     username_pass=deriver.find_element_by_id('com.aixuetang.online:id/et_password')
            #     username_pass.clear()
            #     username_pass.send_keys('930423')
            #     deriver.find_element_by_id('com.aixuetang.online:id/tv_register').click()
            #     if deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip'):
            #         print('zhuceshibai!')
            #     else:
            #        me=deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip').text
            #        print(me)
            username=deriver.find_element_by_id('com.aixuetang.online:id/et_username')
            username.clear()
            username.send_keys('15964636199')
            username_passwored=deriver.find_element_by_id('com.aixuetang.online:id/et_password')
            username_passwored.clear()
            username_passwored.send_keys('li930423')
            deriver.find_element_by_id('com.aixuetang.online:id/tv_login').click()
            time.sleep(2)
            print('yijingdenglu')
            # if deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip'):
            #     print('fail! resion:%s'%(deriver.find_element_by_id('com.aixuetang.online:id/tv_msg_tip').text))
            if deriver.find_element_by_id('com.aixuetang.online:id/user_vip'):
                print('sucess')
                deriver.find_element_by_id('com.aixuetang.online:id/user_setting').click()
                deriver.find_element_by_id('com.aixuetang.online:id/tv_logout').click()
                print('1')
            else:
                print('fail')
        else:
            print('进入失败，请确定定位方式是否正确')
    else:
        print('进入个人中心失败')
        deriver.quit()
except:
    print('启动失败')
    deriver.quit()