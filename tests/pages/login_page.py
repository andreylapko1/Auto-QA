from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_username_input(self):
        return self.driver.find_element(By.ID, "user-name")

    def get_password_input(self):
        return self.driver.find_element(By.ID, "password")

    def login_button(self):
        return self.driver.find_element(By.ID, "login-button")

    def enter_username(self, username_value):
        username_input = self.get_username_input()
        username_input.send_keys(username_value)

    def enter_password(self, password_value):
        password_input = self.get_password_input()
        password_input.send_keys(password_value)

    def click_login_button(self):
        login_button = self.login_button()
        login_button.click()

