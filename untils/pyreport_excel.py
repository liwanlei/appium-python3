# encoding: utf-8
"""
@author: lileilei
@software: PyCharm
@file: pyreport_excel.py
@time: 2017/6/7 8:47
"""
import xlwt
from xlwt import *
from datetime import datetime
from  config.config import *
from  untils.saveresult import parse_result
from untils.log import LOG,logger
from untils.BaseApk import getPhoneInfo
'''生成xlsx的测试报告'''
def yangshi1():
    style = XFStyle()
    fnt = Font()
    fnt.name = u'微软雅黑'
    fnt.bold = True
    style.font = fnt
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style.alignment = alignment  # 给样式添加文字居中属性
    style.font.height = 430  # 设置字体大小
    return style
def yangshi2():
    style1 = XFStyle()
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    style1.alignment = alignment  # 给样式添加文字居中属性
    style1.font.height = 330  # 设置字体大小
    return style1
def yangshi3():
    style1 = XFStyle()
    style1.font.height = 330  # 设置字体大小
    return style1
def yangshique(me):
    if me =='pass':
        style=yangshi1()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['green']
        style.pattern=Pattern
    else :
        style=yangshi2()
        Pattern=xlwt.Pattern()
        Pattern.pattern=xlwt.Pattern.SOLID_PATTERN
        Pattern.pattern_fore_colour=xlwt.Style.colour_map['red']
        style.pattern=Pattern
        return style
@logger('生成测试报告')
def create(filename,testtime,Test_version,devices_list):
    try:
        file = Workbook(filename)
        table = file.add_sheet('测试结果',cell_overwrite_ok=True)
        style=yangshi1()
        for i in range(0, 7):
            table.col(i).width = 380*20
        style1=yangshi2()
        table.write_merge(0,0,0,6,'测试报告',style=style)
        table.write_merge(2,3,0,6,'测试详情',style=style1)
        table.write(4,0,'项目名称',style=style1)
        table.write(5,0,'测试版本',style=style1)
        table.write(6,0,'提测时间',style=style1)
        table.write(7,0,'提测人',style=style1)
        table.write(4,2,'测试人',style=style1)
        table.write(5,2,'测试时间',style=style1)
        table.write(6,2,'审核人',style=style1)
        table.write(8,0,'链接号',style=style1)
        table.write(8,1, '品牌', style=style1)
        table.write(8,2, '设备名', style=style1)
        table.write(8,3, '型号', style=style1)
        table.write(8,4, '版本', style=style1)
        table.write(8,5, '通过', style=style1)
        table.write(8,6, '失败', style=style1)
        table.write(4, 1, Test_Project_name,style=style1)
        table.write(5, 1, Test_version,style=style1)
        table.write(6, 1, testtime,style=style1)
        table.write(7, 1, TiTestuser,style=style1)
        table.write(4, 3, Test_user,style=style1)
        table.write(5, 3, datetime.now().strftime("%Y-%m-%d %HH:%MM"),style=style1)
        table.write(6, 3, "admin",style=style1)
        all_result=[]
        for devices in devices_list:
            fail,pass_a,reslut=parse_result(devices=str(devices))
            all_result.append(reslut)
            de_result=getPhoneInfo(devices=str(devices))
            table.write(9,0,devices, style=style1)
            table.write(9, 1,de_result['brand'], style=style1)
            table.write(9, 2,de_result['device'], style=style1)
            table.write(9, 3,de_result['model'], style=style1)
            table.write(9, 4,de_result['release'], style=style1)
            table.write(9,5,fail, style=style1)
            table.write(9,6,pass_a, style=style1)
        table1 = file.add_sheet('测试详情',cell_overwrite_ok=True)
        table1.write_merge(0,0,0,8,'测试详情',style=style)
        for i in range(0,6):
            table1.col(i).width = 400*20
        table1.write(1,0,'测试用例编号',style=yangshi3())
        table1.write(1,1,'测试模块',style=yangshi3())
        table1.write(1,2,'所需要参数',style=yangshi3())
        table1.write(1,3,'预期',style=yangshi3())
        table1.write(1,4,'结果',style=yangshi3())
        table1.write(1,5,'测试设备',style=yangshi3())
        for i in range(len(all_result)):
            for item in all_result[i]:
                table1.write(i+2, 0,str(eval(item['canshu'])['id']),style=yangshi3())
                table1.write(i+2, 1,str(eval(item['canshu'])['model']),style=yangshi3())
                table1.write(i+2, 2,str(eval(item['canshu'])),style=yangshi3())
                table1.write(i+2, 3,str(eval(item['canshu'])['assert']),style=yangshi3())
                table1.write(i+2, 4, str(item['result']),style=yangshi3())
                table1.write(i+2, 5,str(item['devices']),style=yangshi3())
        file.save(filename)
        LOG.info("测试报告保存成功")
    except Exception as e:
        LOG.error("测试报告生成失败,原因：%s"%e)
