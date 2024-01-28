from selenium.webdriver.common.by import By


class Searchpage:
    _my_account_css = "[title='My Account']"
    _login_link_text = "Login"

    def __init__(self, driver):
        self.driver = driver

    def is_product_displayed(self, product_name):
        return  self.driver.find_element(By.LINK_TEXT, product_name).is_displayed()

    def is_invalid_product(self, message):
        return self.driver.find_element(By.XPATH, f"//p[text()='{message}']").is_displayed()

    def click_my_account(self):
        self.driver.find_element(By.CSS_SELECTOR, self._my_account_css).click()
        return

    def click_login_link(self):
        self.driver.find_element(By.LINK_TEXT, self._login_link_text).click()
        return
