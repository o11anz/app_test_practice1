from selenium.webdriver.common.by import By
import config
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 点击个人
        self.mine = (
            By.XPATH,
            "//android.widget.TextView[@resource-id='com.netease.yanxuan:id/txt_mainpage_tab_title' and @text='个人']",
        )
        # 同意协议
        self.agree = (By.ID, "com.netease.yanxuan:id/check_box")
        # 选择其他登录
        self.other_login = (
            By.XPATH,
            "(//android.widget.ImageView[@resource-id='com.netease.yanxuan:id/img_icon'])[2]",
        )
        # 其他登录方式
        self.other_login_types = (
            By.ID,
            "com.netease.yanxuan:id/newOtherLoginTypes",
        )
        # 邮箱登录
        self.email_login = (
            By.XPATH,
            "(//android.widget.ImageView[@resource-id='com.netease.yanxuan:id/img_icon'])[4]",
        )
        # 账号
        self.account = (By.ID, "com.netease.yanxuan:id/account_edit")
        # 密码
        self.password = (By.ID, "com.netease.yanxuan:id/password_edit")
        # 登录按钮
        self.login_button = (By.ID, "com.netease.yanxuan:id/btn_login_content")
        # 登录成功结果
        self.successful_result = (
            By.XPATH,
            "//android.widget.TextView[@resource-id='com.netease.yanxuan:id/order_tag' and @text='全部订单']",
        )
        # Toast 提示
        self.toast = (By.XPATH, "//android.widget.Toast")
        # 随机弹窗 坐标：[939,90][1035,186]
        self.random_popup = ( By.XPATH,"//*[@bounds='[939,90][1035,186]']")
        # 登陆失败结果
        self.fail_result = (By.XPATH, "//android.widget.Toast")
            #本来是 By.XPATH,"//android.widget.Toast[@text='账号或密码错误']"
            #但是考虑到其他格式的错误，文本内容会变，又要单独写一个这个属性，所以直接删掉


    def click_mine(self):
        """点击我的"""
        self.click(self.mine)

    def click_agree(self):
        """同意协议"""
        checkbox = self.find_clickable(self.agree)
        if str(checkbox.get_attribute("checked")).lower() != "true":
            checkbox.click()

    def click_other_login(self):
        """点击其他登录"""
        self.click(self.other_login)

    def click_other_login_types(self):
        """选择其他登录方式"""
        self.click(self.other_login_types)

    def click_email_login(self):
        """选择邮箱登录"""
        self.click(self.email_login)

    def login(self, account, password):
        """输入账号、密码并点击登录"""
        self.input_text(self.account, account)
        self.input_text(self.password, password)
        self.hide_keyboard()
        self.click(self.login_button)



    def is_login_success(self):
        """出现“全部订单”说明登录成功"""
        return self.is_displayed(self.successful_result, timeout=config.LOGIN_WAIT)

    def get_success_result(self):
        """获取登录成功后的页面文本"""
        return self.get_text(self.successful_result)

#get_xxx_result调用的是get_text而get_text调用的是webdriverwait visibility，失败的这种弹窗捕捉不到，看不见，所以改成
#presence,存在就可以抓取，不管是否可见
    def get_fail_result(self):
        """获取登录失败 Toast，没有则返回空字符串。"""
        return self.get_toast(self.fail_result)

    def get_toast_message(self):
        """读取 Toast 提示，没有则返回空字符串。"""
        return self.get_toast(self.toast, timeout=2)
