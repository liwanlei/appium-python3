'''
  @Description      
  @auther         leizi
  @create          2020-03-13 20:59
'''

from config.config import Test_stf_plan, Test_stf_token
import requests, json


class StfPhoneOpear(object):
    def __init__(self):
        self.test_stf_plan = Test_stf_plan
        self.test_stf_token = Test_stf_token
        self.headers = {"Authorization": "Bearer " + Test_stf_token}

    def getstflist(self) -> list:
        '''
        获取所有的设备
        :return:
        '''
        requests_list = requests.get(Test_stf_plan + "/api/v1/devices", headers=self.headers).text
        allreslut = json.loads(requests_list)
        list_phone = allreslut['devices']
        all_list_dict = []
        for item in list_phone:
            iphone = {}
            iphone['url'] = item['remoteConnectUrl']
            iphone["platform"] = item['platform']
            iphone['version'] = item['version']
            iphone['serial'] = item['serial']
            iphone['use'] = item['using']
            all_list_dict.append(iphone)
        return all_list_dict

    def getonedetail(self, name) -> dict:
        '''
        获取设备详情
        :param name:
        :return:
        '''
        requests_list = requests.get(Test_stf_plan + "/api/v1/devices/" + name, headers=self.headers).text
        allreslut = json.loads(requests_list)
        item = allreslut['devices']
        iphone = {}
        iphone['url'] = item['remoteConnectUrl']
        iphone["platform"] = item['platform']
        iphone['version'] = item['version']
        iphone['serial'] = item['serial']
        return iphone

    def getoneconnecturl(self, name):
        '''
        获取设备远程操作地址
        :param name:
        :return:
        '''
        url = Test_stf_plan + "/api/v1/user/devices/" + name + '/remoteConnect'
        requests_list = requests.post(url,
                                      headers=self.headers).text
        allreslut = json.loads(requests_list)
        item = allreslut['remoteConnectUrl']
        return item

    def oparyonephone(self, name) -> bool:
        '''
        申请设备
        :param name:
        :return:
        '''
        data = {"serial": name}
        self.headers['Content-Type'] = 'application/json'
        requests_list = requests.post(url=Test_stf_plan + "/api/v1/user/devices",
                                      headers=self.headers, data=json.dumps(data)).text
        allreslut = json.loads(requests_list)
        if allreslut['success'] is True:
            return True
        return False

    def removeroneophen(self, name) -> bool:
        '''
        归还设备
        :param name:
        :return:
        '''
        requests_list = requests.delete(Test_stf_plan + "/api/v1/user/devices/" + name,
                                        headers=self.headers).text
        allreslut = json.loads(requests_list)
        if allreslut['success'] is True:
            return True
        return False
