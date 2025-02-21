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

    # driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html") # 1
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/") # 2

    yield driver
    driver.quit()


def test_text(driver):
    iframe = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '(//iframe)')))
    sleep(1)
    driver.switch_to.frame(iframe)
    div = driver.find_element(By.XPATH, '(//*[@class="col-12 py-2"])[@id="content"]')
    p_elements = div.find_elements(By.TAG_NAME, 'p')
    p_texts = [p.text for p in p_elements]

    a = ( text  for text in p_texts if 'semper posuere integer et senectus justo curabitur.' in text)
    a = ' '.join(a)
    assert 'semper posuere integer et senectus justo curabitur.' in a



def test_img(driver):


    wait = WebDriverWait(driver, 10)


    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    sleep(2)
    image = driver.find_element(By.XPATH, '//*[@src="images/high_tatras_min.jpg"]')

    target = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#trash')))

    actions = ActionChains(driver)
    actions.drag_and_drop(image, target).perform()

    trash_items = driver.find_elements(By.CSS_SELECTOR, "#trash [class='ui-widget-content ui-corner-tr ui-draggable ui-draggable-handle']")
