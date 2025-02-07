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
    options.add_argument('--window-size=1920x1080')
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://itcareerhub.de/ru")

    yield driver
    driver.quit()



def test_display(driver):
    driver.maximize_window()
    test_lst = []
    ich_logo = driver.find_element(By.CSS_SELECTOR, '[data-original="https://static.tildacdn.net/tild3333-3534-4535-a465-643634653734/Group_3793.svg"]')
    sleep(2)
    test_lst.append(ich_logo.is_displayed())
    progs = driver.find_element(By.XPATH, '(//a[text()="Программы"])[1]')
    sleep(2)
    test_lst.append(progs.is_displayed())
    payment = driver.find_element(By.XPATH, '(//a[text()="Способы оплаты"])[1]')
    sleep(2)
    test_lst.append(payment.is_displayed())
    news = driver.find_element(By.XPATH, '(//a[text()="Новости"])[1]')
    sleep(2)
    test_lst.append(news.is_displayed())
    about_us = driver.find_element(By.XPATH, '(//a[text()="О нас"])[1]')
    sleep(2)
    test_lst.append(about_us.is_displayed())
    sleep(5)
    reviews = driver.find_element(By.XPATH, '(//a[text()="Отзывы"])[1]')
    sleep(2)
    test_lst.append(reviews.is_displayed())
    assert all(test_lst)


def test_change_language_button(driver):
    de_button = driver.find_element(By.XPATH, '(//a[text()="de"])[1]')
    de_button.click()
    current_url = driver.current_url
    if current_url == "https://itcareerhub.de/":
        sleep(2)
        ru_button = driver.find_element(By.XPATH, '(//a[text()="ru"])[1]')
        ru_button.click()
        sleep(2)
        assert current_url == 'https://itcareerhub.de/ru'

def test_phone_text(driver):
    button_phone = driver.find_element(By.CSS_SELECTOR, '[src="https://static.tildacdn.net/tild3933-3337-4237-a439-336463393463/Group_3800.svg"]')
    button_phone.click()
    sleep(2)
    txt = button_phone.get_attribute('outerText')
    assert  txt == 'Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами'

