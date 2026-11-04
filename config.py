"""项目配置：设备、Appium 地址、目录、等待时间。"""

from pathlib import Path

# 项目路径
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "log"
REPORT_DIR = BASE_DIR / "report"
SCREENSHOT_DIR = REPORT_DIR / "screenshots"

LOGIN_DATA_FILE = DATA_DIR / "login_data.json"
LOG_FILE = LOG_DIR / "appium.log"

# Appium 和设备
APPIUM_SERVER_URL = "http://127.0.0.1:4723"

# 第一次启动app
FIRST_APP_CONFIG = {
    "APP_PACKAGE" : "com.netease.yanxuan",
    "APP_ACTIVITY"  : ".SplashActivityDefault",
}

# app本身配置
APP_CONFIG = {
    "APP_PACKAGE" : "com.netease.yanxuan",
    "APP_ACTIVITY"  : ".SplashActivityDefault",
    "noReset" : True, # 不清除数据，保留登陆状态
}

# 兼容 practice 旧页面中使用的 config.APP_PACKAGE / config.APP_ACTIVITY
APP_PACKAGE = FIRST_APP_CONFIG["APP_PACKAGE"]
APP_ACTIVITY = FIRST_APP_CONFIG["APP_ACTIVITY"]

DEVICE_CONFIG = {
    # automationName 由 UiAutomator2Options 自动设置
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "mumu",
    "appPackage": APP_CONFIG["APP_PACKAGE"],
    "appActivity": APP_CONFIG["APP_ACTIVITY"],
    "noReset": True,
}

# 等待时间（秒）
WAIT_TIME = 10
SHORT_WAIT = 5
LOGIN_WAIT = 20
