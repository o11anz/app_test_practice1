"""公共工具：驱动、日志、读取 JSON、截图。"""

import json
import logging
from datetime import datetime

from appium import webdriver
from appium.options.android import UiAutomator2Options

import config

def get_driver():
    """创建 Appium 驱动。"""
    options = UiAutomator2Options().load_capabilities(config.CAPABILITIES)
    return webdriver.Remote(
        command_executor=config.APPIUM_SERVER_URL,
        options=options,
    )


def get_logger():
    """创建控制台 + 文件日志，重复调用不会重复添加 handler。"""
    config.LOG_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("app")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    file = logging.FileHandler(config.LOG_FILE, encoding="utf-8")
    file.setFormatter(formatter)
    logger.addHandler(file)

    return logger


#def read_json(file_path):
 #   """读取 JSON 文件。"""
  #  with open(file_path, "r", encoding="utf-8") as file:
   #     return json.load(file)

def read_json(file_name):
    """
    读取JSON并转换为格式为 [(), (), ...] 的列表
    :param file_name: json文件名
    :return: 列表
    """
    data = []  # 空列表
    file_path = config.BASE_DIR / "data" / file_name  # JSON文件路径

    # 打开JSON文件
    with open(file_path, mode='r', encoding='utf-8') as f:
        # 读取JSON文件并解析为Python对象【列表套字典】
        tmp = json.load(f)

        for i in tmp:
            a = tuple(i.values())
            data.append(a)

        # 返回列表
        return data

def read_json_single(file_name):
    """
    读取单列 JSON，返回 [值, 值, ...]
    例如：
        [{"search": "毛巾"}, {"search": "纸巾"}]
    转成：
        ["毛巾", "纸巾"]
    """
    data = read_json(file_name)
    return [item[0] for item in data]

def save_screenshot(driver, name):
    """保存失败截图。"""
    config.SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"{name}_{datetime.now():%Y%m%d_%H%M%S}.png"
    path = config.SCREENSHOT_DIR / filename
    driver.save_screenshot(str(path))
    return path

def quit_app_driver(driver):
    if driver:
        driver.quit()
