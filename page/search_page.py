from base import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # 搜索框
        self.search_frame = (By.XPATH,"//android.widget.TextSwitcher[@resource-id='com.netease.yanxuan:id/tv_home_search']")
        # 内容框
        self.search_content = (By.ID, "com.netease.yanxuan:id/search_input")
        # 搜索按钮
        self.search_button = (By.XPATH, "//android.widget.TextView[@resource-id='com.netease.yanxuan:id/tv_search_button']")
        # 搜索成功结果
        self.successful_result = (By.XPATH,"(//android.widget.TextView[@resource-id='com.netease.yanxuan:id/tv_goods_name'])[1]")

    # 点击搜索框
    def search_frame_click(self):
        self.click(self.search_frame)

    # 输入搜索内容
    def search_content_input(self, text):
        self.input_text(self.search_content, text)

    # 点击搜索按钮
    def search_button_click(self):
        self.click(self.search_button)

    # 返回搜索成功结果
    def get_search_successful_result(self):
        return self.get_text(self.successful_result)

    # 搜索
    def search(self, text):
        self.click(self.search_frame)
        self.input_text(self.search_content, text)
        self.click(self.search_button)