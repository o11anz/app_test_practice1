"""公共页面操作基类：定位、点击、输入、判断、滑动。"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
from tools import get_logger, save_screenshot


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        # 注意：这里用的是显式等待时间 WAIT_TIME，不是隐式等待
        self.wait = WebDriverWait(driver, config.WAIT_TIME)

    def _current_activity(self):
        """获取当前页面名称，定位失败时写进日志。"""
        try:
            return self.driver.current_activity
        except Exception:
            return "unknown"

    # ---------- 元素查找 ----------
    def find_element(self, locator, timeout=None):
        """定位单个元素，失败时记录日志。"""
        wait_time = timeout or config.WAIT_TIME
        try:
            self.logger.info(f"定位元素: {locator}")
            return WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as error:
            self.logger.error(
                f"定位元素失败: {locator} | 等待: {wait_time}秒 | "
                f"当前页面: {self._current_activity()} | 原因: {error}",
                exc_info=True,
            )
            raise

    def find_elements(self, locator, timeout=None):
        """定位多个元素，失败时记录日志。"""
        wait_time = timeout or config.WAIT_TIME
        try:
            self.logger.info(f"定位多个元素: {locator}")
            return WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except Exception as error:
            self.logger.error(
                f"定位多个元素失败: {locator} | 等待: {wait_time}秒 | "
                f"当前页面: {self._current_activity()} | 原因: {error}",
                exc_info=True,
            )
            raise

    def find_clickable(self, locator, timeout=None):
        """等待元素可点击，失败时记录日志。"""
        wait_time = timeout or config.WAIT_TIME
        try:
            self.logger.info(f"等待元素可点击: {locator}")
            return WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable(locator)
            )
        except Exception as error:
            self.logger.error(
                f"元素不可点击: {locator} | 等待: {wait_time}秒 | "
                f"当前页面: {self._current_activity()} | 原因: {error}",
                exc_info=True,
            )
            raise

    # 兼容之前的调用写法
    def find(self, locator):
        return self.find_element(locator)

    def find_all(self, locator):
        return self.find_elements(locator)

    # ---------- 常用操作 ----------
    def click(self, locator):
        self.logger.info(f"点击元素: {locator}")
        self.find_clickable(locator).click()
        return self

    def click_if_exists(self, locator, timeout=2):
        """可选弹窗用：存在就点，不存在就跳过。"""
        try:
            self.logger.info(f"尝试点击可选元素: {locator}")
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
            return True
        except Exception as error:
            # 可选弹窗不存在是正常情况，所以只记 debug
            self.logger.debug(
                f"可选元素不存在或不可点击: {locator} | 等待: {timeout}秒 | 原因: {error}"
            )
            return False

    def input_text(self, locator, text, clear=True):
        # 只记录定位器和文本长度，不把密码等原文写进日志
        self.logger.info(f"输入文本: {locator} | 文本长度: {len(str(text))}")
        element = self.find_clickable(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        return self

    def get_text(self, locator):
        text = self.find_element(locator).text
        self.logger.info(f"获取文本: {locator} | 内容: {text}")
        return text

    def get_toast(self, locator, timeout=3):
        """
        获取 Toast、Snackbar 等特殊弹窗的文本。

        Toast 经常没有正常的可见边界，所以这里用 presence，
        不能用 visibility；弹窗没出现时返回空字符串。
        """
        try:
            element = WebDriverWait(self.driver, timeout, 0.1).until(
                EC.presence_of_element_located(locator)
            )
            text = element.text
            self.logger.info(f"获取弹窗文本: {locator} | 内容: {text}")
            return text
        except Exception as error:
            self.logger.debug(
                f"未获取到弹窗文本: {locator} | 等待: {timeout}秒 | 原因: {error}"
            )
            return ""

    # ---------- 判断 ----------
    def is_displayed(self, locator, timeout=None):
        wait_time = timeout or config.WAIT_TIME
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.info(f"元素可见: {locator}")
            return True
        except Exception as error:
            self.logger.debug(
                f"元素不可见: {locator} | 等待: {wait_time}秒 | 原因: {error}"
            )
            return False

    # ---------- 滑动 ----------
    def swipe(self, start_x, start_y, end_x, end_y, duration=500):
        self.logger.info(
            f"滑动屏幕: ({start_x},{start_y}) -> ({end_x},{end_y}) | 时长: {duration}ms"
        )
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        return self

    def swipe_up(self, duration=500):
        size = self.driver.get_window_size()
        w, h = size["width"], size["height"]
        return self.swipe(w // 2, int(h * 0.75), w // 2, int(h * 0.25), duration)

    def swipe_down(self, duration=500):
        size = self.driver.get_window_size()
        w, h = size["width"], size["height"]
        return self.swipe(w // 2, int(h * 0.25), w // 2, int(h * 0.75), duration)

    # ---------- 其他 ----------
    def back(self):
        self.logger.info("按下返回键")
        self.driver.back()
        return self

    def hide_keyboard(self):
        try:
            self.driver.hide_keyboard()
            self.logger.info("收起软键盘")
        except Exception as error:
            self.logger.debug(f"没有可收起的软键盘: {error}")
        return self

    def take_screenshot(self, name):
        path = save_screenshot(self.driver, name)
        self.logger.info(f"保存截图: {path}")
        return path
