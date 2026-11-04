class TestOrder:
    """订单测试"""

    def test_order(self, app_order):
        """订单测试"""
        # app_order 已经完成加购并创建好 OrderPage
        app_order.order()

        # 断言

        # 截图
        # app_order.take_screenshot("order_ok")
