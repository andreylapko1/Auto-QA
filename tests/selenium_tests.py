from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) ### Chrome

#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))





driver.get("https://itcareerhub.de/ru")
sleep(2)
driver.maximize_window()
sleep(1)
about_link = driver.find_element(By.LINK_TEXT, "Программы")
about_link.click()


# driver.save_screenshot("screenshot.png")




