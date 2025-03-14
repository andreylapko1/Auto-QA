from time import sleep
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from orange.pages.dashboard_page import DashboardPage
from orange.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()



@allure.title('Successfully logged in')
def test_successful_login(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
    with allure.step('Send login'):
        login_page.send_username('Admin')
    with allure.step('Send password'):
        login_page.send_password('admin123')
    with allure.step('Click loggin button'):
        login_page.click_login_button()
    with allure.step('Assert check Dashboard'):
        try:
            assert dashboard_page.get_dashboard_text() == 'Dashboard1'
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="Success Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise


