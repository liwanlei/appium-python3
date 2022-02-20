'''
  @Description      
  @auther         leizi
'''
import  sys,copy
import unittest
from io import StringIO as StringIO
TestResult = unittest.TestResult
class MyResult(TestResult):
    def __init__(self, verbosity=1, trynum=0):
        #默认次数是0
        TestResult.__init__(self)
        self.outputBuffer = StringIO()
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity
        self.trynnum = trynum
        self.result = []
        self.trys=0
        self.istry=False
        self.isprintlog=True


    def startTest(self, test):
        TestResult.startTest(self, test)
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr

    def complete_output(self):
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        #判断是否要重试
        if self.istry is True :
            #如果执行的次数小于重试的次数 就重试
            if self.trys < self.trynnum :
                #删除最后一个结果
                reslut = self.result.pop(-1)
                #判断最后一个结果
                if reslut[0] == 1:
                    #如果是错误就把错误的个数减掉
                    self.failure_count -= 1
                else:
                    # 如果是失败，就把失败的次数减掉
                    self.error_count -= 1
                sys.stderr.write('{}:用例正在重试中。。。' .format(test.id())+ '\n')

                #深copy用例
                test = copy.copy(test)

                #重试次数增加+1
                self.trys += 1
                #是否展示结果
                self.isprintlog=False
                # 重新测试
                test(self)
            else:
                #是否重试
                self.istry=False
                #重试次数
                self.trys =0
                #是否打印日志
                self.isprintlog=True
        self.complete_output()

    def addSuccess(self, test):
        #成功就不要重试
        self.istry = False
        #成功次数加1
        self.success_count += 1
        #成功结果假如
        TestResult.addSuccess(self, test)
        #打印
        output = self.complete_output()
        #结果增加
        self.result.append((0, test, output, ''))
        #是否打印详细日志
        if self.verbosity > 1:
            #打印详细日志
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            #不打印详细日志
            sys.stderr.write('.')

    def addError(self, test, err):
        if self.isprintlog is True:
            self.istry = True
            self.error_count += 1
            TestResult.addError(self, test, err)
            _, _exc_str = self.errors[-1]
            output = self.complete_output()
            self.result.append((2, test, output, _exc_str))
            if self.verbosity > 1:
                sys.stderr.write('E  ')
                sys.stderr.write(str(test))
                sys.stderr.write('\n')
            else:
                sys.stderr.write('E ')
        else:
            self.istry = True
            self.error_count += 1
            TestResult.addError(self, test, err)
            _, _exc_str = self.errors[-1]
            output = self.complete_output()
            self.result.append((2, test, output, _exc_str))

    def addFailure(self, test, err):
        if self.isprintlog is True:
            self.istry = True
            TestResult.startTestRun(self)
            self.failure_count += 1
            TestResult.addFailure(self, test, err)
            _, _exc_str = self.failures[-1]
            output = self.complete_output()
            self.result.append((1, test, output, _exc_str))
            if self.verbosity > 1:
                sys.stderr.write('F  ')
                sys.stderr.write(str(test))
                sys.stderr.write('\n')
            else:
                sys.stderr.write('F ')
        else:
            self.istry = True
            TestResult.startTestRun(self)
            self.failure_count += 1
            TestResult.addFailure(self, test, err)
            _, _exc_str = self.failures[-1]
            output = self.complete_output()
            self.result.append((1, test, output, _exc_str))

    def stop(self) -> None:
        pass