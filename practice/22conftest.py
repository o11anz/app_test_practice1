"""pytest 公共 fixture：驱动、测试数据、失败截图。"""

import pytest

import config
from tools import get_driver, get_logger, read_json, save_screenshot

logger = get_logger()


@pytest.fixture
def driver():
    logger.info("创建 Appium 会话")
    app_driver = get_driver()
    yield app_driver
    app_driver.quit()
    logger.info("关闭 Appium 会话")


@pytest.fixture(scope="session")
def login_data():
    if not config.LOGIN_DATA_FILE.exists():
        pytest.skip("缺少 data/login_data.json，请先填写登录账号和密码")
    return read_json(config.LOGIN_DATA_FILE)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """用例失败时自动截图。"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        app_driver = getattr(item, "funcargs", {}).get("driver")
        if app_driver is not None:
            path = save_screenshot(app_driver, item.name)
            report.sections.append(("失败截图", str(path)))
