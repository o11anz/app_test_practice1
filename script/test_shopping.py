

class TestShopping:
    def test_shopping_success(self, app_shopping, logger):
        # 调用方法
        app_shopping.shopping()
        # 打印日志
        result = app_shopping.get_successful_result()
        logger.info(f"添加购物车结果{result}")
        # 断言
        assert "加入购物车成功" in result
        # 截图
        app_shopping.take_screenshot(f"添加购物车结果{result}")