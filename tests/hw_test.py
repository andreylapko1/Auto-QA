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

    # driver.get("http://uitestingplayground.com/textinput") # task 1
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html") # task 2

    yield driver
    driver.quit()


# def test_button_click(driver):
#     wait = WebDriverWait(driver, 10)
#     input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[placeholder="MyButton"]')))
#     input_field.send_keys("ITCH")
#     button = driver.find_element(By.ID, "updatingButton")
#     button.click()
#     assert button.text == 'ITCH'


def test_alt_img(driver):
    wait = WebDriverWait(driver, 15)
    last_img = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[alt="landscape"]')))
    third_alt = driver.find_element(By.CSS_SELECTOR, '#award')

    assert third_alt.get_attribute('alt') == 'award'



