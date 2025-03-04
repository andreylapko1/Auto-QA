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

from tests.pages import inventory_page
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage, ByThing

DATA = ('standard_user', 'secret_sauce')

@pytest.fixture()
def driver():
    # service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=ChromeService())
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()



def test_check_cards(driver):
    login_page = LoginPage(driver)
    login_page.success_login('standard_user', 'secret_sauce')
    inventory_page = InventoryPage(driver)
    assert inventory_page.get_quantity_cards() == 6


def test_check_all_cards_are_displayed(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    login_page.success_login('standard_user', 'secret_sauce')
    assert inventory_page.is_all_cards_displayed() == True


def test_not_empty_title(driver):
    LoginPage(driver).success_login(*DATA)
    inventory_page = InventoryPage(driver)
    assert inventory_page.check_not_empty_title()



