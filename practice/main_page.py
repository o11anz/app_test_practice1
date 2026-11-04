"""首页：底部导航栏。"""

from appium.webdriver.common.appiumby import AppiumBy

import config
from base.base_page import BasePage


class MainPage(BasePage):
    PROFILE_TAB = (
        AppiumBy.XPATH,
        f"//*[@resource-id='{config.APP_PACKAGE}:id/txt_mainpage_tab_title' "
        "and @text='个人']",
    )

    def open_profile(self):
        """点击底部“个人”Tab。"""
        self.click(self.PROFILE_TAB)
