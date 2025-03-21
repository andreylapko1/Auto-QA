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


    driver.get("http://www.uitestingplayground.com/ajax")

    yield driver
    driver.quit()


def test_request(driver):

    trigger_button = driver.find_element(By.CSS_SELECTOR, "[class='btn btn-primary']")
    trigger_button.click()

    wait = WebDriverWait(driver, 16)
    response_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bg-success")))

    assert response_text.text == "Data loaded with AJAX get request."


