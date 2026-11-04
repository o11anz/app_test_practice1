import pytest

import tools


class TestLogin:
    """登录测试"""

    arg_names = "account", "password", "expect_result", "photo_result"

    @pytest.mark.parametrize(arg_names, tools.read_json("login_data.json"))
    def test_login(
        self,
        app_login,
        logger,
        account,
        password,
        expect_result,
        photo_result,
    ):
        # 调用登录
        app_login.login(account, password)

        # 获取结果
        if expect_result == "全部订单":
            result = app_login.get_success_result()
        else:
            result = app_login.get_fail_result()

        logger.info(f"登录结果:{result}")

        # 断言
        assert expect_result in result

        # 截图
        app_login.take_screenshot(photo_result)
