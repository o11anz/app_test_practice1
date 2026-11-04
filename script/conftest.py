import tools
from page import LoginPage
from page.home_page import HomePage
import pytest
from page.shopping_page import ShoppingPage
from page.search_page import SearchPage
from page.order_page import OrderPage
from appium.options.android import UiAutomator2Options
from appium import webdriver
import time
from config import *


def restart_app(driver):
    """重启 App，保留登录数据，同时回到启动入口。"""
    driver.terminate_app(APP_PACKAGE)
    driver.activate_app(APP_PACKAGE)

# @pytest.fixture(scope = "function")
# def app_driver():
#     driver = tools.get_driver()
#     yield driver
#     tools.quit_app_driver(driver)
@pytest.fixture
def app_driver():
    # 配置移动端设备信息
    des_caps = {**DEVICE_CONFIG, **APP_CONFIG}
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=option)
    # 返回值
    yield driver
    # 暂停3秒
    time.sleep(3)
    # 关闭驱动
    driver.quit()

@pytest.fixture
def app_first_driver():
    # 第一次登录使用干净状态
    des_caps = {
        **DEVICE_CONFIG,
        **FIRST_APP_CONFIG,
        "noReset": False,
    }
    # 初始化设备配置信息
    option = UiAutomator2Options().load_capabilities(des_caps)
    # 创建驱动对象
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=option)
    # 返回值
    yield driver
    # 暂停3秒
    time.sleep(3)
    # 关闭驱动
    driver.quit()


@pytest.fixture
def logger():
    return tools.get_logger()


@pytest.fixture(scope = "function")
def app_home(app_driver):
    # 强制启动 App 入口，避免上一条用例把页面留在支付页/商品页
    restart_app(app_driver)

    homepage = HomePage(app_driver)
    # 进入首页
    homepage.GoHome()


@pytest.fixture(scope = "function")
def app_first_home(app_first_driver):
    # 第一次登录的 driver 也先进入首页
    restart_app(app_first_driver)
    HomePage(app_first_driver).GoHome()


@pytest.fixture(scope = "function")
def app_login(app_first_driver, app_first_home):
    loginpage = LoginPage(app_first_driver)
    # 处理随机弹窗
    loginpage.click_if_exists(loginpage.random_popup)
    # 点击个人，点击同意协议，点击选择其他登录，点击选择登录方式,点击邮箱登录
    loginpage.click_mine()
    loginpage.click_agree()
    loginpage.click_other_login()
    loginpage.click_other_login_types()
    loginpage.click_email_login()
    return loginpage


@pytest.fixture(scope = "function")
def app_search(app_driver, app_home):
    searchpage = SearchPage(app_driver)
    return searchpage


@pytest.fixture(scope = "function")
def app_shopping(app_driver, app_search, app_home):
    shoppingpage = ShoppingPage(app_driver)
    app_search.search("毛巾")
    yield shoppingpage
    # 不依赖返回按钮，直接回到首页
    restart_app(app_driver)


@pytest.fixture(scope = "function")
def app_order(app_driver, app_shopping):
    # 让订单测试自己准备购物车，不依赖 test_shopping 的执行顺序
    app_shopping.shopping()
    restart_app(app_driver)

    yield OrderPage(app_driver)

    # 订单结束可能停在支付页，强制回首页
    restart_app(app_driver)
