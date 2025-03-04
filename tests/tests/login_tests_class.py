from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage


@pytest.fixture(scope="module")
def driver():
    # service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=ChromeService())
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_success_login_class(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'Failed to login'

    inventory_list = inventory_page.inventory_list_is_displayed()
    assert inventory_list, 'Not displayed'


def test_invalid_password_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauc')
    login_page.click_login_button()
    assert login_page.h3_error_message_text() == 'Epic sadface: Username and password do not match any user in this service'



def test_blocked_user_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('locked_out_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert login_page.h3_error_message_text() == 'Epic sadface: Sorry, this user has been locked out.'


def test_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.click_login_button()
    assert login_page.h3_error_message_text() == 'Epic sadface: Password is required'

def test_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()
    assert login_page.h3_error_message_text() == 'Epic sadface: Username is required'