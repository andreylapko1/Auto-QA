from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920x1080')
    # options.add_argument('--headless')

    service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)



    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    yield driver
    driver.quit()


def test_login(driver):
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="username"]')))
    username.send_keys("Admin")

    password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="password"]')))
    password.send_keys("admin123")

    login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
    login_btn.click()
    sleep(5)
