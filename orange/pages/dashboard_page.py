from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_dashboard(self):
        return self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h6')))

    def get_dashboard_text(self):
        return self.get_dashboard().text