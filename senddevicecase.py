'''
  @Description      
  @auther         leizi
'''

'''
1.获取设备信息
2.获取用例
3.分配给设备执行
4.可以不同的方式去选择执行不一样的测试用例

'''
import unittest
from multiprocessing import Pool


class Parmer(unittest.TestCase):
    def __init__(self, methodName='runTest', parme=None):
        super(Parmer, self).__init__(methodName)
        self.parme = parme

    def parametrize(self, testcase_klass, parame):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            for i in parame:
                suite.addTest(testcase_klass(methodName=name, parme=i))
        return suite


class regtest(Parmer):
    def setUp(self) -> None:
        print('test  reg interface')

    def testreg(self):
        print(self.parme)


class logintest(Parmer):
    def setUp(self) -> None:
        print("test login interface")

    def testreg(self):
        print(self.parme)


from untils.tytest import MyResult


def ruun(parame, testcase):
    test_suit = unittest.TestSuite()
    name = Parmer().parametrize(testcase, parame)
    test_suit.addTest(name)  # 扩展的其他的测试用例均这样添加
    rse = MyResult(trynum=10)
    test_suit.run(rse)


if __name__ == "__main__":

    case = [{'name': "login", "case": [{'phone1': "baiejing"},
                                       {'phone1': "baiejing"}]},
            {"name": "regin", 'case': [{'phone2': "baiejing"},
                                       {'phone2': "baiejing"}]}]
    name = Pool()
    relustlist = []
    for i in range(len(case)):
        if i//1==0:
            relust = name.apply_async(ruun, [case[i]['case'],logintest, ])
            relustlist.append(relust)
        else:
            relust = name.apply_async(ruun, [case[i]['case'], regtest,])
            relustlist.append(relust)
    # 进程池关闭
    name.close()
    for i in relustlist:
        # 等待进程执行完毕
        i.wait()
