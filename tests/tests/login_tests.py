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



@pytest.fixture
def driver():
    service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_success_login(driver):
    username_input_field = driver.find_element(By.ID, "user-name")
    username_input_field.send_keys("standard_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", 'Failed to login'

    inventory_list = driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory_list.is_displayed()


def test_blocked_user(driver):
    username_input_field = driver.find_element(By.ID, "user-name")
    username_input_field.send_keys("locked_out_user")
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_msg = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert 'Epic sadface: Sorry, this user has been locked out.' in error_msg.text


def test_login_without_user(driver):
    password_input_field = driver.find_element(By.ID, "password")
    password_input_field.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_msg = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert 'Epic sadface: Username is required' in error_msg.text

def test_login_without_password(driver):
    username_input_field = driver.find_element(By.ID, "user-name")
    username_input_field.send_keys("locked_out_user")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    error_msg = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
    assert 'Epic sadface: Password is required' in error_msg.text