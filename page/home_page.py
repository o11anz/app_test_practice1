from base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #启动页同意协议
        self.home_agree = (By.ID, "com.netease.yanxuan:id/btn_alert_positive")
        #启动页跳过
        self.home_pass = (By.XPATH,"//android.widget.TextView[@text='跳过']")


    #进入首页
    def GoHome(self):
        self.click_if_exists(self.home_agree)
        self.click_if_exists(self.home_pass)
        time.sleep(3)
