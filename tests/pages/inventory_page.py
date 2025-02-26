from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_inventory_list_is_displayed(self):
        inventory_lst = self.driver.find_element(By.CLASS_NAME, "inventory_list")
        return inventory_lst.is_displayed()

