# test_login.py
import pytest
from framework.pages.login_page import LoginPage
from framework.driver_factory import create_driver


class TestLogin:
    def test_successful_login(self):
        driver = create_driver()
        login_page = LoginPage(driver)
        login_page.click_login_button()
        login_page.enter_email()
        login_page.enter_passwd()
        driver.quit()
