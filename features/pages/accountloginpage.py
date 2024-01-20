from selenium.webdriver.common.by import By


class Accountloginpage:
    _email_address_id = "input-email"
    _password_id = "input-password"
    _login_button_css = "[value='Login']"

    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email):
        self.driver.find_element(By.ID, self._email_address_id).clear()
        self.driver.find_element(By.ID, self._email_address_id).send_keys(email)
        return

    def enter_password(self, password):
        self.driver.find_element(By.ID, self._password_id).clear()
        self.driver.find_element(By.ID, self._password_id).send_keys(password)
        return

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self._login_button_css).click()
        return

    def is_warning_message_displayed(self, message):
        assert self.driver.find_element(By.XPATH, f"//*[text()='{message}']").is_displayed()
