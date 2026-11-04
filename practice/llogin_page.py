"""登录页：协议、其他登录、邮箱登录。"""

from appium.webdriver.common.appiumby import AppiumBy

import config
from base.base_page import BasePage


class LoginPage(BasePage):
    AGREEMENT_CHECKBOX = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/check_box",
    )
    OTHER_LOGIN_ENTRY = (
        AppiumBy.XPATH,
        "(//android.widget.ImageView[@resource-id="
        f"'{config.APP_PACKAGE}:id/img_icon'])[2]",
    )
    MORE_LOGIN_TYPES = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/newOtherLoginTypes",
    )
    EMAIL_LOGIN_ICON = (
        AppiumBy.XPATH,
        "(//android.widget.ImageView[@resource-id="
        f"'{config.APP_PACKAGE}:id/img_icon'])[4]",
    )
    ACCOUNT_INPUT = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/account_edit",
    )
    PASSWORD_INPUT = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/password_edit",
    )
    LOGIN_BUTTON = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/btn_login_content",
    )
    TOAST = (AppiumBy.XPATH, "//android.widget.Toast")

    def wait_until_loaded(self):
        """等待登录页加载完成。"""
        self.find_clickable(self.AGREEMENT_CHECKBOX)

    def accept_agreement(self):
        """勾选协议；已勾选时不重复点击。"""
        checkbox = self.find_clickable(self.AGREEMENT_CHECKBOX)
        if str(checkbox.get_attribute("checked")).lower() != "true":
            checkbox.click()

    def click_other_login(self):
        self.click(self.OTHER_LOGIN_ENTRY)

    def click_more_login_types(self):
        self.click(self.MORE_LOGIN_TYPES)

    def choose_email_login(self):
        self.click(self.EMAIL_LOGIN_ICON)

    def input_account(self, account):
        self.input_text(self.ACCOUNT_INPUT, account)

    def input_password(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def submit_login(self):
        self.hide_keyboard()
        self.click(self.LOGIN_BUTTON)

    def login_with_email(self, account, password):
        """完整邮箱登录流程。"""
        self.wait_until_loaded()
        self.accept_agreement()
        self.click_other_login()
        self.click_more_login_types()
        self.choose_email_login()
        self.input_account(account)
        self.input_password(password)
        self.submit_login()

    def is_login_success(self):
        """账号输入框消失，说明已经离开登录页。"""
        return not self.is_displayed(self.ACCOUNT_INPUT, timeout=config.LOGIN_WAIT)

    def get_toast_message(self):
        """读取 Toast 提示，没有则返回空字符串。"""
        try:
            if self.is_displayed(self.TOAST, timeout=2):
                return self.get_text(self.TOAST)
        except Exception:
            pass
        return ""
