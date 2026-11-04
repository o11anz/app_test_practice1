from appium.webdriver.common.appiumby import AppiumBy
from base.base_page import BasePage


class OrderPage(BasePage):
    """订单页面"""

    def __init__(self, driver):
        super().__init__(driver)

        # 点击购物车图标
        self.cart_icon_loc = (
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="购物车"]',
        )

        # 点击结算按钮
            #1.直接定位
            # self.settlement_btn_loc = (AppiumBy.XPATH,'//android.widget.TextView[@text="结算(1)"]'),

            #2.利用结算文本包含定位
            # self.settlement_btn_loc = (AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"结算")]')

            #3.定位结算按钮框
        self.settlement_btn_loc = (
            AppiumBy.XPATH,
            '//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[5]',
        )

        # 点击提交订单按钮
        self.order_btn_loc = (
            AppiumBy.ID,
            'com.netease.yanxuan:id/order_btn',
        )
        # 获取位置请求
        self.location_request = (AppiumBy.XPATH,
                                 '//android.widget.Button[@resource-id="com.netease.yanxuan:id/btn_alert_positive"]')

    def order(self):
        """提交订单"""
        self.click(self.cart_icon_loc)
        self.click(self.settlement_btn_loc)
        self.click(self.order_btn_loc)

    # 允许位置请求获取
    def allow_location_request(self):
        self.click_if_exists(self.location_request)
