from appium.webdriver.common.appiumby import By
from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et4"]')
    PASSWORD_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="com.code2lead.kwad:id/Et5"]')
    LOGIN_BUTTON = (By.XPATH, '//android.widget.Button[@content-desc="Btn6"]')

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def enter_email(self):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys('admin@gmail.com')

    def enter_passwd(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys('admin123')
