from appium import webdriver
from appium.options.android import UiAutomator2Options
from framework.caps import capabilities


def create_driver():
    appium_server_url = 'http://localhost:4723/wd/hub'
    return webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
