""" 
@author: lileilei
@file: phone.py 
@time: 2018/1/22 9:59 
"""
import os
import subprocess


# 得到手机信息
def get_phone_info(devices):
    cmd = "adb -s " + devices + " shell cat /system/build.prop "
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    l_list = {}
    release = "ro.build.version.release="  # 版本
    model = "ro.product.model="  # 型号
    brand = "ro.product.brand="  # 品牌
    device = "ro.product.device="  # 设备名
    for line in phone_info:
        for i in line.split():
            temp = i.decode()
            if temp.find(release) >= 0:
                l_list["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                l_list["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                l_list["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                l_list["device"] = temp[len(device):]
                break
    print(l_list)
    return l_list


# 得到最大运行内存
def get_men(devices):
    cmd = "adb -s " + devices + " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) + 1:].replace("kB", "").strip()
            break
    return int(men_total)


# 得到几核cpu
def get_cpu(devices):
    cmd = "adb -s " + devices + " shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"


# 得到手机分辨率
def get_pix(devices):
    result = os.popen("adb -s " + devices + " shell wm size", "r")
    return result.readline().split("Physical size:")[1]
