from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver:
    def __init__(self, base_url):
        self.driver = webdriver.Firefox()
        self.base_url = base_url

    def exit(self):
        self.driver.close()

    def navigate(self, path):
        self.driver.get(f"{self.base_url}/{path}")

    def find_by_css(self, css_selector_str):
        return self.driver.find_elements(By.CSS_SELECTOR, css_selector_str)

    def find_by_id(self, id):
        return self.driver.find_element(By.ID, id)

    def click(self, id):
        element = self.find_by_id(id)
        element.click()
