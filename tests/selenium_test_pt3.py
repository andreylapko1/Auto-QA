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

    driver.get("https://crossbrowsertesting.github.io/todo-app.html")

    yield driver
    driver.quit()



def test_pic(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.XPATH, '(//p[text()="Done!"])[1]')))
    third_alt = driver.find_element(By.CSS_SELECTOR, '#award')
    assert third_alt.get_attribute('alt') == 'award'


def test_checkbox(driver):
    li_1 = driver.find_element(By.NAME, 'todo-1')
    li_1.click()
    span = driver.find_element(By.CSS_SELECTOR, '[name="todo-1"] ~ span')
    text_decoration = driver.execute_script("return window.getComputedStyle(arguments[0]).textDecoration;", span)
    assert span.get_attribute('class') == 'done-true', f'{text_decoration}'