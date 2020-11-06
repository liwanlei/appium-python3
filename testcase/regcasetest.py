from appium import webdriver
import ddt, os, time
from untils.Parmeris import Parmer
from untils.log import LOG
from untils.disapp import make_dis
from untils.gettestdata import huoqu_test
from funtions.regpub import RegFuntion
from untils.huoqu_xingneng import caijicpu, getnencun
from untils.recording_txt import write_recording
from config.config import TestappPackage

path = os.getcwd()

path_test_case=os.path.join("path",'data')
testcasedata = path_test_case + 'testcase_data.xlsx'
data_test = huoqu_test(testcasedata, index=1)
from untils.saveresult import save_result


@ddt.ddt
class regtest(Parmer):
    def __init__(self, parm, methodName='runTest'):
        super(regtest, self).__init__(methodName)
        self.port = parm['port']
        LOG.info(parm)
        self.parm = parm

    """这是reg测试用例"""

    def setUp(self):
        """ setup """
        self.dis_app = make_dis(Testplatform=self.parm['platformName'],
                                TestplatformVersion=self.parm['platformVersion'],
                                Testdevicesname=self.parm['deviceName'],
                                TestappPackage=self.parm['appPackage'],
                                TestappActivity=self.parm['appActivity'])
        self.deriver = webdriver.Remote('http://127.0.0.1:' + self.port + '/wd/hub', self.dis_app)
        LOG.info('reg测试用例开始执行')

    def tearDown(self):
        """ tearDown  """
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        time.sleep(15)
        self.deriver.quit()

    @ddt.data(*data_test)
    def testreg(self, data_test):
        """reg测试"""
        regfun = RegFuntion(deriver=self.deriver)
        self.assertuen = regfun.reg(**data_test)
        cpu = caijicpu(packagename=TestappPackage, devices=self.parm['deviceName'])
        neicun = getnencun(packagename=TestappPackage, devices=self.parm['deviceName'])
        write_recording(cpu=cpu, neicun=neicun, devices=str(self.parm['deviceName']))
        if data_test['assert'] == self.assertuen:
            shebei = self.parm['udid']
            data = shebei + '&' + 'pass' + '&' + str(data_test)
            save_result(data)
        else:
            shebei = self.parm['udid']
            data = shebei + '&' + 'fail'
            save_result(data)
