from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_inventory_list(self):
        return self.driver.find_element(By.CLASS_NAME, "inventory_list")

    def inventory_list_is_displayed(self):
        return self.get_inventory_list().is_displayed()

    def get_cards(self):
        return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

    def get_quantity_cards(self):
        return len(self.get_cards())

    def is_all_cards_displayed(self):
        for card in self.get_cards():
            if not card.is_displayed():
                return False
        else:
            return True

    def get_all_cards_title(self):
        return self.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')

    def check_not_empty_title(self):
        return all(bool(el.text) for el in self.get_all_cards_title())


class ByThing():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def by_elements(self):
        buttons = self.driver.find_elements(By.TAG_NAME, '.btn')
        print(len(buttons))



