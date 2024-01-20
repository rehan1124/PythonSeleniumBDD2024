from selenium.webdriver.common.by import By


class Myaccountpage:

    def __init__(self, driver):
        self.driver = driver

    def is_user_logged_in(self, link_text):
        assert self.driver.find_element(By.LINK_TEXT, link_text).is_displayed()
