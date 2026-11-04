"""启动页：隐私协议、启动引导。"""

from appium.webdriver.common.appiumby import AppiumBy

import config
from base.base_page import BasePage


class LaunchPage(BasePage):
    AGREE_BUTTON = (
        AppiumBy.ID,
        f"{config.APP_PACKAGE}:id/btn_alert_positive",
    )
    SKIP_BUTTON = (AppiumBy.XPATH, "//*[@text='跳过']")

    def handle_launch(self):
        """处理启动弹窗；没有弹窗时自动跳过。"""
        self.click_if_exists(self.AGREE_BUTTON, timeout=config.WAIT_TIME)
        self.click_if_exists(self.SKIP_BUTTON, timeout=config.SHORT_WAIT)
