import time

from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 配置移动端设备信息
des_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "mumu",
    "appPackage": "com.netease.yanxuan",
    "appActivity": ".SplashActivityDefault"
}

option = UiAutomator2Options().load_capabilities(des_caps)

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=option)

time.sleep(3)#浏览器刚创建出来无法点击，先等一下
#点击同意协议
driver.find_element(By.ID, "com.netease.yanxuan:id/btn_alert_positive").click()
#点击跳过
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "android.widget.TextView"))).click()
#点击个人
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@resource-id='com.netease.yanxuan:id/txt_mainpage_tab_title' and @text='个人']"))).click()
#显示同意协议(这种一长串的0000是错的，不能用这个定位"0000-000..."）
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com.netease.yanxuan:id/check_box"))).click()
#显示点击其他登录（这种class的值也有很多重复，也不行）
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//android.widget.ImageView[@resource-id='com.netease.yanxuan:id/img_icon'])[2]"))).click()
#选择其他登录方式
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com.netease.yanxuan:id/newOtherLoginTypes"))).click()
#选择邮箱登录xpath
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//android.widget.ImageView[@resource-id='com.netease.yanxuan:id/img_icon'])[4]"))).click()
#登录账号
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com.netease.yanxuan:id/account_edit"))).send_keys("b3227749640@163.com")
#输入密码
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com.netease.yanxuan:id/password_edit"))).send_keys("Lbwnb666@")
#点击登录按钮
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "com.netease.yanxuan:id/btn_login_content"))).click()

#time.sleep(5)
#driver.find_element(By.XPATH, "//androidx.compose.ui.platform.ComposeView[@resource-id='com.netease.yanxuan:id/compose_kingkong']/android.view.View/android.view.View[1]").click()
#time.sleep(3)
#driver.swipe(649,1590,649,1400)


time.sleep(3)

driver.quit()