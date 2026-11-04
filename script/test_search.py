import tools
import pytest

arg_names = "search"
@pytest.mark.parametrize(arg_names, tools.read_json_single("search_data.json"))
class TestSearch():
    def test_01_search_success(self, app_driver, app_search, logger, search):
        try:
            # 准备数据
            # 调用方法
                # 点击搜索框
            app_search.search_frame_click()
                # 输入搜索内容
            app_search.search_content_input(search)
                # 点击搜索按钮
            app_search.search_button_click()
            #记录日志
            logger.info(f"搜索结果:{search}")
            # 断言
            assert search in app_search.get_search_successful_result()
            # 截图
            app_search.take_screenshot(f"搜索结果{search}.png")
        except Exception as e:
            # 截图
            app_search.take_screenshot(f"搜索失败{search}.png")
            # 抛出异常
            raise e
