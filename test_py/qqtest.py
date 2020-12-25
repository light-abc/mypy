from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time

class QQPlatform():
    def __init__(self):
        self.url = "https://open.qq.com/login"
        self.username = "username"
        self.password = "password"
        self.hub = 'hub地址'
        self.browser = webdriver.Remote(
            command_executor='http://%s:4444/wd/hub'%(self.hub),
            desired_capabilities=DesiredCapabilities.CHROME)
        self.browser.maximize_window()

    def login(self):
        print("开始登录")
        self.browser.get(self.url)
        time.sleep(0.2)
        self.browser.implicitly_wait(30)
        self.browser.switch_to.frame('login_frame')
        self.browser.find_element_by_id("switcher_plogin").click()
        time.sleep(0.2)
        self.browser.find_element_by_id("u").send_keys(self.username)
        self.browser.find_element_by_id("p").send_keys(self.password)
        time.sleep(0.2)
        self.browser.find_element_by_id("login_button").click()
        WebDriverWait(self.browser,15).until(lambda the_driver: the_driver.find_element_by_id('_leftSidebar').is_displayed())
        print("登录成功")

    def upload(self,apk):
        # 新功能
        print("开始上传")
        apkName=apk.split('/')[-1]
        handle = self.browser.current_window_handle
        self.browser.find_element_by_class_name('cover').click()
        self.browser.find_element_by_partial_link_text('更新安装包').click()
        print(self.browser.current_url)
        handles=self.browser.window_handles
        for newhandle in handles:
            if newhandle != handle:
                self.browser.switch_to.window(newhandle)
        print(self.browser.current_url)
        try:
            self.browser.find_element_by_class_name("webuploader-element-invisible").send_keys(apk)
            self.browser.implicitly_wait(20)
        except:
            print("软件包上传失败")
            exit(2)
        # 下一步: 待优化
        time.sleep(30)
        # verifyTextPresent(pattern):校验当前页面是否出现该文字
        # WebDriverWait(self.browser, 30).until(
        #     lambda the_driver: the_driver.find_element(By.XPATH, '//p[text()="%s")]'%(apkName)).is_displayed())
        print("软件包上传成功")

    def submit(self,isTest):
        print("开始发布")
        self.browser.find_element_by_id('j-submit-btn').click()
        time.sleep(3)
        if isTest:
            # 测试打开
            self.browser.find_element_by_class_name('j-confirm-no').click()
        else:
            # 正式使用打开
            self.browser.find_element_by_id('j-confirm-yes').click()
        time.sleep(1)
        print("软件包已发布")

    def close(self):
        time.sleep(2)
        print("退出浏览器")
        time.sleep(2)
        self.browser.quit()
        print("应用发布结束")

if __name__ == '__main__':
    apk="/data/apks/_V_2.0.7_300_2020-09-27.apk"
    isTest=True
    qq = QQPlatform()
    qq.login()
    qq.upload(apk=apk)
    qq.submit(isTest=isTest)
    qq.close()
