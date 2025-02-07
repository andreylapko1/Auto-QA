import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) ### Chrome


@pytest.fixture
def driver():
    options = Options()
    # options.add_argument('--window-size=1920x1080')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://suninjuly.github.io/cats.html")
    yield driver
    driver.quit()


def tests_cats_page(driver):
    header = driver.find_element(By.TAG_NAME, "h1")
    print(header.text)
    assert header.text == "Cat memes"


def test_time(driver):
    time_first_card = driver.find_element(By.XPATH, '//div[@class="col-sm-4"][1]//small')
    print(time_first_card.text)
    assert time_first_card.text == "8 mins"


def test_last_text(driver):
    last_text = driver.find_element(By.XPATH, '//div[@class="col-sm-4"][last()]//p')
    assert last_text.text == "I love you so much"

def test_first_card_is_displayed(driver):
    first_card = driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(1)')
    assert first_card.is_displayed()


def test_photo_icon_is_displayed(driver):
    photo_icon = driver.find_element(By.TAG_NAME, 'svg')
    assert photo_icon.is_displayed()


def test_check_quantity_imgs(driver):
    cards_imgs = driver.find_elements(By.CSS_SELECTOR, ".row img")
    assert len(cards_imgs) == 6


def test_check_availability_cards(driver):
    cards_availability = driver.find_elements(By.CSS_SELECTOR, ".col-sm-4")
    assert len(cards_availability) == 6


def test_all_displayed_cards(driver):
    cards_availability = driver.find_elements(By.CSS_SELECTOR, ".col-sm-4")
    is_disp = all(card.is_displayed() for card in cards_availability)
    assert is_disp









