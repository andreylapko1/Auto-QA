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


class BaseTest:
    def __init__(self):
        self.driver = self.driver()


    @pytest.fixture()
    def driver(self):
        # service = ChromeService(executable_path='C:/Users/andre/Desktop/chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(service=ChromeService())
        self.driver.get("https://www.saucedemo.com/")


        yield
        self.driver.quit()
