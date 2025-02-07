from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920x1080')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://suninjuly.github.io/registration1.html")

    yield driver
    driver.quit()



def test_success_test_registration_all_fields(driver):
    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Andrey")
    second_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    second_name.send_keys("Andreev")
    email = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    email.send_keys("asd@gmail.com")
    phone = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your phone:']")
    phone.send_keys("+91123456789")
    address = driver.find_element(By.CSS_SELECTOR, "[placeholder='Input your address:']")
    address.send_keys('New York')
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()
    current_url = driver.current_url
    assert current_url == 'https://suninjuly.github.io/registration_result.html?'


def test_regirst_with_empty_firstname(driver):
    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()
    assert first_name.get_attribute("validationMessage") == "Заполните это поле."


def test_emply_lasntame(driver):
    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Andrey")
    email = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    email.send_keys("asd@gmail.com")
    second_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    assert second_name.get_attribute("validationMessage") == "Заполните это поле."




def test_empty_email(driver):
    first_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    first_name.send_keys("Andrey")
    second_name = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    second_name.send_keys("Andreev")
    email = driver.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()
    assert email.get_attribute("validationMessage") == "Заполните это поле."