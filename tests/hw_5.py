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
    actions = ActionChains(driver)

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe.demo-frame')))
    # iframe = driver.find_element(By.TAG_NAME, "iframe")
    # driver.switch_to.frame(iframe)
    sleep(2)

    image = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#gallery > li')))
    img_1 = image[0]

    target = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#trash')))
    actions.drag_and_drop(img_1, target).perform()
    sleep(1)
    assert len(driver.find_elements(By.CSS_SELECTOR, '#gallery > li')) == len(image) - 1

