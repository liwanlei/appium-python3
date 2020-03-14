'''关于appium的一个简单的封装'''


class deriver_fengzhuang():
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, fangfa, lujing):
        if fangfa == 'id':
            se = self.driver.find_elements_by_id(lujing)
        elif fangfa == 'xpath':
            se = self.driver.find_element_by_xpath(lujing)
        elif fangfa == 'css':
            se = self.driver.find_element_by_css_selector(lujing)
        elif fangfa == 'and':
            se = self.driver.find_element_by_android_uiautomator(
                'new Uiselector().%s' % lujing)  # 这里在使用的时候比如使用text，那么这里的lujing为text('123')
        elif fangfa == 'class':
            se = self.driver.find_element_by_class_name(lujing)
        elif fangfa == 'name':
            se = self.driver.find_element_by_name(lujing)
        elif fangfa == 'acces':
            se = self.driver.find_element_by_accessibility_id(lujing)
        elif fangfa == 'text':
            se = self.driver.find_element_by_link_text(lujing)
        elif fangfa == 'partial':
            se = self.driver.find_element_by_partial_link_text(lujing)
        elif fangfa == 'tag':
            se = self.driver.find_element_by_tag_name(lujing)
        else:
            raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
        return se

    def find_elemens(self, fangfa, lujing):
        try:
            if fangfa == 'id':
                se = self.driver.find_elements_by_id(lujing)
            elif fangfa == 'xpath':
                se = self.driver.find_elements_by_xpath(lujing)
            elif fangfa == 'css':
                se = self.driver.find_elements_by_css_selector(lujing)
            elif fangfa == 'and':
                se = self.driver.find_elements_by_android_uiautomator(
                    'new Uiselector().%s' % lujing)  # 这里在使用的时候比如使用text，那么这里的lujing为text('123')
            elif fangfa == 'class':
                se = self.driver.find_elements_by_class_name(lujing)
            elif fangfa == 'name':
                se = self.driver.find_elements_by_name(lujing)
            elif fangfa == 'acces':
                se = self.driver.find_elements_by_accessibility_id(lujing)
            elif fangfa == 'text':
                se = self.driver.find_elements_by_link_text(lujing)
            elif fangfa == 'partial':
                se = self.driver.find_elements_by_partial_link_text(lujing)
            elif fangfa == 'tag':
                se = self.driver.find_elements_by_tag_name(lujing)
            else:
                raise NameError('no element,please send tag,xpath,text,id,css,id,tag')
            return se
        except Exception as e:
            return e

    def ins(self, path):  # 安装app
        self.driver.install_app(path)

    def rem(self, baoming):  # 卸载app
        self.driver.remove_app(baoming)

    def rem_ios(self, bundleId):  # ios
        self.driver.remove_app(bundleId)

    def close(self):  # 关闭app
        self.driver.close_app()

    def reset(self):  # 重置app
        self.driver.reset()

    def hide_keyb(self):  # 隐藏键盘
        self.driver.hide_keyboard()

    def send_keyevent(self, event):  # 只有安卓有
        self.driver.keyevent(event=event)

    def sned_press_keycode(self, keycode):  # 安卓有
        self.driver.press_keycode(keycode=keycode)

    def long_press_keycode(self, keycode):  # 长按发送
        self.driver.long_press_keycode(keycode)

    def current_activity(self):
        activity = self.driver.current_activity()
        return activity

    def wait_activity(self, activity, times, interval=1):
        self.driver.wait_activity(activity, time=times, interval=1)

    def run_back(self, second):
        self.driver.background_app(seconds=second)

    def is_app_installed(self, baoming):  # ios需要buildid
        self.driver.is_app_installed(baoming)

    def launch_app(self):  # 启动app
        self.driver.launch_app()

    def start_acti(self, app_package, app_activity):
        self.driver.start_activity(app_package, app_activity)

    def ios_lock(self, locktime):
        self.driver.lock(locktime)

    def yaoshouji(self):
        self.driver.shake()

    def open_tongzhi(self):  # 安卓api 18以上
        self.driver.open_notifications()

    def renturn_network(self):  # 返回网络
        network_type = self.driver.network_connection
        return network_type

    def set_network_type(self, type):
        from appium.webdriver.connectiontype import ConnectionType
        if type == 'wifi' or type == 'WIFI' or type == 'w' or type == 'WIFI_ONLY':
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif type == 'data' or type == 'DATA' or type == 'd' or type == 'DATA_ONLY':
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif type == 'ALL' or type == 'all' or type == 'a' or type == 'ALL_NETWORK_ON':
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        elif type == 'NO' or type == 'no' or type == 'n' or type == 'NO_CONNECTION':
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif type == 'AIRPLANE_MODE' or type == 'air' or type == 'ar' or type == 'fly':
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        else:
            raise NameError('plase wifi ,data,all,no,fly')

    def run_shurufa(self):
        shurufa = self.driver.available_ime_engines
        return shurufa

    def shuru_active(self):
        check = self.driver.is_ime_active
        return check

    def active_shurufa(self, engine):
        self.driver.activate_ime_engine(engine)

    def close_shurufa(self):
        self.driver.deactivate_ime_engine()

    def return_shurufa(self):
        shurufa_name = self.driver.active_ime_engine
        return shurufa_name

    def open_dingwei(self):
        self.driver.toggle_location_services()

    def set_weizhi(self, weidu, jingdu, haiba):
        self.driver.set_location(weidu, jingdu, haiba)

    def get_size(self):
        size = self.driver.se.size
        return size

    def text(self):
        text = self.driver.text
        return text

    def is_dis(self):
        dis = self.driver.se.is_displayed()
        return dis

    def screet(self, filename):
        self.driver.get_screenshot_as_base64(filename)

    def clos(self):
        self.driver.close()

    def kill(self):
        self.driver.quit()

    def screet_wind(self):
        me = self.driver.get_screenshot_as_file()
        return me  # 返回 ture,flase

    def get_wiow_size(self):  # 获取窗口大小
        return self.driver.get_window_size()

    def fangda(self, element):  # 放大
        self.driver.zoom(element)

    def suoxiao(self, element):  # 缩小
        self.driver.pinch(element)

    def kuaisuhuadong(self, s_x, s_y, e_x, e_y):  # 从一点到另一点
        self.driver.flick(s_x, s_y, e_x, e_y)

    def huadong(self, s_x, s_y, e_x, e_y, duration=None):
        self.driver.swipe(s_x, s_y, e_x, e_y)

    def chumo(self, x, y, duration=None):
        self.driver.tap([(x, y)], 500)

    def scroll(self, x, y):  # 滚动元素
        self.driver.scroll(x, y)

    def drag_and_drop(self, e1, e2):  # 移动元素
        self.driver.drag_and_drop(e1, e2)

    def contexts_is(self):  # 可用
        self.driver.contexts()

    def push(self, data, path):
        self.driver.push_file(data, path)

    def pull(self, path):
        self.driver.pull_file(path)

    def wait(self, seconde):
        self.driver.wait_activity(seconde)

    def send_key(self, pas):
        self.driver.send_keys(pas)
