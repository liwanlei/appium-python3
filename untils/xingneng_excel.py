# encoding: utf-8  
""" 
@author: lileilei 
@file: xingneng_excel.py 
@time: 2018/1/20 12:53 
"""
from untils.log import LOG,logger
import  xlsxwriter
@logger('保存cpu，流量，内存')
def getcpu(cishu,start_cpu,recv_list,send_list,total_list,Pass_list):
	try:
		workbook=xlsxwriter.Workbook('cpu_liu_men_report.xlsx')
		worksheet=workbook.add_worksheet('cpu')
		worksheet_liulang=workbook.add_worksheet('liulang')
		worksheet_men=workbook.add_worksheet('men')
		bold=workbook.add_format({'bold':1})
		headings=['次数','cpu占用率']
		headings_liuliang=['次数','上传流量','下载流量','总计']
		headings_men=['次数','Pass占百分比']
		data_cpu=[cishu,start_cpu]
		data_liuliang=[cishu,recv_list,send_list,total_list]
		data_men=[cishu,Pass_list]
		worksheet_liulang.write_row('A1',headings_liuliang,bold)
		worksheet_liulang.write_column('A2',data_liuliang[0])
		worksheet_liulang.write_column('B2',data_liuliang[2])
		worksheet_liulang.write_column('C2',data_liuliang[1])
		worksheet_liulang.write_column('D2',data_liuliang[3])
		worksheet_men.write_row('A1',headings_men,bold)
		worksheet_men.write_column('A2',data_men[0])
		worksheet_men.write_column('B2',data_men[1])
		worksheet.write_row('A1',headings,bold)
		worksheet.write_column('A2',data_cpu[0])
		worksheet.write_column('B2',data_cpu[1])
		chart1 = workbook.add_chart({'type': 'scatter',
								'subtype': 'straight_with_markers'})
		chart2=workbook.add_chart({'type': 'scatter',
								'subtype': 'straight_with_markers'})
		chart3=workbook.add_chart({'type': 'scatter',
								'subtype': 'straight_with_markers'})
		chart3.add_series({
			'name':'=men!$B$1',
			'categories': '=men!$A$2:$A$%s'%(len(cishu)+1),
			'values': '=men!$B$2:$B$%s'%(len(cishu)+1),
			})
		chart2.add_series({
			'name':'=liulang!$B$1',
			'categories': '=liulang!$A$2:$A$%s'%(len(cishu)+1),
			'values': '=liulang!$B$2:$B$%s'%(len(cishu)+1),

			})
		chart1.add_series({
			'name':'=cpu!$B$1',
			'categories': '=cpu!$A$2:$A$%s'%(len(cishu)+1),
			'values': '=cpu!$B$2:$B$%s'%(len(cishu)+1),
			})
		chart2.add_series({
			'name':'=liulang!$C$1',
			'categories':'=liulang!$A$2:$A$%s'%(len(cishu)),
			 'values':'=liulang!$C$2:$C$%s'%(len(cishu)),
			})
		chart2.add_series({
			'name':'=liulang!$D$1',
			'categories':'=liulang!$A$2:$A$%s'%(len(cishu)),
			 'values':'=liulang!$D$2:$D$%s'%(len(cishu)),
			})
		chart2.set_title({'name':'流量统计图'})
		chart2.set_x_axis({'name':'次数'})
		chart2.set_y_axis({'name':'流量：k'})
		chart2.set_style(11)
		chart3.set_title({'name':'内存占有率统计图'})
		chart3.set_x_axis({'name':'次数'})
		chart3.set_y_axis({'name':'pass值：k'})
		chart3.set_style(11)
		worksheet_men.insert_chart('F2',chart3,{'x_offset':60,'y_offset':60})
		worksheet_liulang.insert_chart('F2',chart2,{'x_offset': 60, 'y_offset': 60})
		chart1.set_title({'name':'cpu占用率'})
		chart1.set_x_axis({'name':"次数"})
		chart1.set_y_axis({'name':'占用:%'})
		chart1.set_style(11)
		worksheet.insert_chart('D2', chart1, {'x_offset': 60, 'y_offset': 60})
		workbook.close()
		LOG.info('保存流量，内存等采集数据，成功')
	except:
		LOG.info('保存流量，内存等采集数据，失败:%s'%Exception)