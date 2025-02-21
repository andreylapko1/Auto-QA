from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import math


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920x1080')
    # options.add_argument('--headless')

    service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    # driver.get('http://suninjuly.github.io/redirect_accept.html')  # first test
    driver.get("https://crossbrowsertesting.github.io/hover-menu.html")


    yield driver
    driver.quit()



def test_switch(driver):
    redirect_btn = driver.find_element(By.TAG_NAME, "button")
    redirect_btn.click()
    sleep(3)
    print(driver.window_handles)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.current_window_handle)
    mean = int(driver.find_element(By.ID, "input_value").text)
    rad = math.radians(mean)
    result = math.log(abs(12 * math.sin(rad)))
    inpt = driver.find_element(By.TAG_NAME, "input")
    inpt.send_keys(f'{result}')
    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()
    sleep(3)


def test_hover(driver):
    wait = WebDriverWait(driver, 10)
    dropdown = driver.find_element(By.LINK_TEXT, "Dropdown")
    actions = ActionChains(driver)
    actions.move_to_element(dropdown).perform()
    drop_menu_secondary_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[@class='dropdown-toggle'])[2]")))
    actions.move_to_element(drop_menu_secondary_menu).perform()
    sleep(3)