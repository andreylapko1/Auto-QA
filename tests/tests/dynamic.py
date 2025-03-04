
from math import sin, log
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

    driver.get("https://suninjuly.github.io/explicit_wait2.html")
    yield driver
    driver.quit()


def test_success_test(driver):
    price_locator = (By.CSS_SELECTOR, '#price')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element(price_locator,"100"))
    driver.find_element(By.CSS_SELECTOR, "#book").click()
    value = int(driver.find_element(By.ID, "input_value").text)
    result = log(abs(12 * sin(value)))
    form = driver.find_element(By.CLASS_NAME, 'form-control')
    form.send_keys(str(result))
    driver.find_element(By.ID, 'solve').click()
    sleep(2)
    alert = wait.until(EC.alert_is_present())
    assert 'Congrats' in alert.text



