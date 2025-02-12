from time import sleep

# import pytest
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920x1080')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(15)
    driver.get("http://www.uitestingplayground.com/ajax")

    yield driver
    driver.quit()

def test_response(driver):
    btn = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
    btn.click()
    # wait = WebDriverWait(driver, 15)
    txt = driver.find_element(By.CLASS_NAME, "bg-success")
    assert txt.text == 'Data loaded with AJAX get request.'

