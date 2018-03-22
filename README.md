# appium-python3进行app自动化测试

###   目前很多的公司无论招聘，还是在工作中，也会对自动化有要求，但是ui的自动化的产出低，但是在回归场景，的确能够减少人工的重复工作。自动化测试不一定快。目前很多公司会认为自动化测试就是快，这个是个误区。
##   1.项目概述
###   使用目前较为流行的UI自动化测试工具Appium，
###  语言选择python3，利用ddt进行数据驱动，
###  yaml管理项目的定位，Excel管理测试用例，
###  unittest进行组织测试用例，测试设备选择夜神模拟器,
###  测试报告使用BSTestRunner进行测试用例完成后测试报告的生成。
### 依赖第三方包见requirements.txt。
##   2.目录简介：
###      a.business：业务相关的处理
###      b.config：配置相关
###      c.data：业务相关，yaml文件存储功能定位相关的，用例采用Excel管理。
###      d.testcase：测试用例模块
###      c.testlog:测试过程中的测试日志
###      d.testpang:测试过程中的部分截图
###      e.testreport：测试报告，性能收集结果存储地方。
###      f.testsuite:组织测试用例。
###      g.untils：   公共的工具模块。
###      h.main.py   ui自动化测试的主脚本

-------

目前存在的不足，只能支持单台设备，单线程跑测试用例，性能测试数据目前收集存放在txt文档中没有进行分析
---------

## 3.效果展示图
###  整体结构
![Alt text](https://github.com/liwanlei/appium-python3/blob/master/img/zhutijiegou.png)
###  运行后展示
#### 控制台展示

![Alt text](https://github.com/liwanlei/appium-python3/blob/master/img/yunxing.png)

#### 测试日志

![Alt text](https://github.com/liwanlei/appium-python3/blob/master/img/logrizhi.png)

#### 测试报告


![Alt text](https://github.com/liwanlei/appium-python3/blob/master/img/ceshibaogao.png)

####  采集性能测试结果

![Alt text](https://github.com/liwanlei/appium-python3/blob/master/img/caijixingneng.png)
