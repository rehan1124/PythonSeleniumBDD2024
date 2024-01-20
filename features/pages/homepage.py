from selenium.webdriver.common.by import By


class Homepage:
    _search_input_name = "search"
    _search_button = "[id='search'] button"

    def __init__(self, driver):
        self.driver = driver

    def enter_product_name(self, product_name):
        self.driver.find_element(By.NAME, self._search_input_name).send_keys(product_name)
        return

    def click_search_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self._search_button).click()
        return
