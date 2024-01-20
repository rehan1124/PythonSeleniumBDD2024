from selenium.webdriver.common.by import By


class Searchpage:

    def __init__(self, driver):
        self.driver = driver

    def is_product_displayed(self, product_name):
        assert self.driver.find_element(By.LINK_TEXT, product_name).is_displayed()

    def is_invalid_product(self, message):
        assert self.driver.find_element(By.XPATH, f"//p[text()='{message}']").is_displayed()
