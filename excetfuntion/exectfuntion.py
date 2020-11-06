""" 
@author: lileilei
@file: exectfuntion.py 
@time: 2018/4/17 13:46 
"""
from untils.operyaml import open_da
from untils.log import logger, LOG
import time
from untils.py_app import deriver_fengzhuang as feng

'''解析测试步骤，按照需求进行测试用例
   默认的定位的最后的一组为断言
'''


@logger('解析测试步骤')
class Makeappcase():
    def __init__(self, deriver, path):
        self.deriver = deriver
        self.path = path

    def open_file(self):
        return open_da(path=self.path)

    def exce_case(self, **kwargs):
        data = self.open_file()['data']
        case_der = feng(driver=self.deriver)
        for i in range(len(data) - 1):
            f = case_der.find_elemens(lujing=data[i]['element_info'], fangfa=data[i]['find_type'])
            if data[i]['operate_type'] == 'click':
                f[int(data[i]['index'])].click()
            elif data[i]['operate_type'] == 'text':
                f[int(data[i]['index'])].text
            elif data[i]['operate_type'] == 'send_key':
                f[int(data[i]['index'])].clear()
                f[int(data[i]['index'])].set_value(kwargs.get(data[i]['key']))
            else:
                LOG.info('请检查您的测试步骤')
            i += 1
            time.sleep(8)
        f = case_der.find_elemens(lujing=data[-1]['element_info'], fangfa=data[-1]['find_type'])
        if data[-1]['operate_type'] == 'text':
            duanyan = {'code': 0, 'data': f[int(data[-1]['index'])].text}
        else:
            duanyan = {'code': 1, 'data': "请检查您的测试步骤最后一步为断言用的"}
            LOG.info('请检查您的测试步骤最后一步为断言用的')
        return duanyan
