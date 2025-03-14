from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_username_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, 'username')))

    def get_password_input(self):
        return self.wait.until(EC.presence_of_element_located((By.NAME, 'password')))

    def get_login_button(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[type="submit"]')))

    def send_username(self, username):
        self.get_username_input().send_keys(username)

    def send_password(self, password):
        self.get_password_input().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'