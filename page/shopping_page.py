from base import BasePage
from selenium.webdriver.common.by import By


class ShoppingPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 页面内第一个商品
        self.product = (By.XPATH,"(//android.widget.TextView[@resource-id='com.netease.yanxuan:id/tv_goods_name'])[1]")
        # 获取位置请求
        self.location_request = (By.XPATH,'//android.widget.Button[@resource-id="com.netease.yanxuan:id/btn_alert_positive"]')
        # “加入购物车”按钮1
        #self.get_cart1 = (By.XPATH,'//android.widget.TextView[@resource-id="com.netease.yanxuan:id/button" and @text="加入购物车"]')
        #这里一直点不进去就是因为这个按钮是一个复合按钮，按钮1定位到的路径中仔细看看，他既包含了1，也包含了2，把2的删掉就是1的
        self.get_cart1 = (By.XPATH,'//android.widget.TextView[@text="加入购物车"]')
        # “加入购物车”按钮2
        self.get_cart2 = (By.ID,'com.netease.yanxuan:id/button')
        # 成功结果
        self.successful_result = (By.XPATH,'//android.widget.Toast')
            # 本来是 By.XPATH,"//android.widget.Toast[@text='加入购物车成功']"
            # 但是考虑到其他格式的弹窗，文本内容会变，又要单独写一个这个属性，所以直接删掉(但是写了也可以
            # 即Toast 文案不是“加入购物车成功”，可能是#已加入购物车
                # 添加成功
                # 请选择规格
                # 请先登录
                # 返回按钮1
            #并且也可能是和login里面一样的错误，方法写错了，即ec.visibility抓不住这个弹窗（就是这个原因）
        self.back_button1 = (By.XPATH,'//android.widget.TextView[@resource-id="com.netease.yanxuan:id/nav_left_text"]')
        # 返回按钮2
        self.back_button2 = (By.XPATH,'//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/search_bar_return"]')
        # 返回按钮3
        self.back_button3 = (By.XPATH,'//android.widget.ImageView[@resource-id="com.netease.yanxuan:id/search_bar_return"]')

    # 允许位置请求获取
    def allow_location_request(self):
        self.click_if_exists(self.location_request, timeout=5)

    # 进入商品详情页
    def enter_product(self):
        self.click(self.product)

    # 点击按钮1
    def click_get_cart1(self):
        self.click(self.get_cart1)

    # 点击按钮2
    def click_get_cart2(self):
        self.click(self.get_cart2)

    # 获取成功结果
    def get_successful_result(self):
        """获取加购结果 Toast，没有则返回空字符串。"""
        return self.get_toast(self.successful_result)

    # 返回首页
    def back_home(self):
        self.click(self.back_button1)
        self.click(self.back_button2)
        self.click(self.back_button3)

    # 加入购物车
    def shopping(self):
        self.click(self.product)
        self.click_if_exists(self.location_request, timeout=5)
        self.click(self.get_cart1)
        self.click(self.get_cart2)
