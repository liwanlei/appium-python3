'''
@author: lileilei
@file: Parmeris.py
@time: 2018/9/21 12:38
'''
'''uittest的再次封装'''
import unittest


class Parmer(unittest.TestCase):
    def __init__(self, methodName='runTest', parme=None):
        super(Parmer, self).__init__(methodName)
        self.parme = parme

    def parametrize(testcase_klass, param=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(methodName=name, parm=param))
        return suite
