"""Page 层统一出口。"""

from practice.launch_page import LaunchPage
from .login_page import LoginPage
from practice.main_page import MainPage

__all__ = ["LaunchPage", "LoginPage", "MainPage"]
