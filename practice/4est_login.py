import time

from page import LoginPage
from page.home_page import HomePage
from page.login_page import LoginPage
import tools


class TestLogin:
    #准备数据
    #(前后置，已fixture）

    def test_01_login_success(self, app_login,app_driver,logger):
        #准备数据
        #调用方法
        app_login.login("b3227749640@163.com","Lbwnb666@")
        #打印结果
        result = app_login.get_success_result()
        logger.info(f"登陆结果:{result}")
        #断言
        assert "全部订单" in result
        #截图
        app_login.take_screenshot("login_success.png")

    def test_02_login_fail_pwdError(self, app_login,app_driver,logger):
        # 准备数据
        # 调用方法
        app_login.login("b3227749640@163.com", "Lbwnb66@")
        # 打印结果
        result = app_login.get_fail_result()
        logger.info(f"登陆结果:{result}")
        # 断言
        assert "账号或密码错误" in result
        # 截图
        app_login.take_screenshot("login_pwdfail.png")

    def test_03_login_fail_actError(self, app_login,app_driver,logger):
        # 准备数据
        # 调用方法
        app_login.login("b3227749640163.com", "Lbwnb666@")
        # 打印结果
        result = app_login.get_fail_result()
        logger.info(f"登陆结果:{result}")
        # 断言
        assert "账号格式错误" in result
        # 截图
        app_login.take_screenshot("login_actfail.png")