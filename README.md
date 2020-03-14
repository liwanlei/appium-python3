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
###      2.1 config：配置相关
###      2.2 data：用例存放Excel管理，dingwei下面需要写成测试步骤的逻辑。
###      2.3 exctfuntion 根据测试文件里面的测试步骤形成相应的测试逻辑
###      2.4 funtions：根据测试逻辑相关和exctfuntion下的形成测试步骤后组合成测试用例
###      2.5 testcase:根据功能模块 形成的测试用例加入相应的测试数据 组成测试用例
###      2.6 testlog:测试过程的日志
###      2.7 testreport：测试报告，性能收集结果存储地方。
###      2.8 testsuite:组织测试用例。
###      2.9 untils：   公共的工具模块。
###      2.10 main.py   ui自动化测试的主脚本

# 友情推荐本人其他开源代码：
#      1.python app自动化测试平台版本：https://github.com/liwanlei/UFATestPlan
#      2.python接口测试框架：https://github.com/liwanlei/jiekou-python3
#      3.python接口测试平台版本：https://github.com/liwanlei/FXTest
#      4.python+flask 做后台，实现微信小程序：https://github.com/liwanlei/webchat_app

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
