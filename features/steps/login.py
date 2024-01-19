from behave import *
from selenium.webdriver.common.by import By


@given(u'User navigates to login page')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[title='My Account']").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'User enters credentials')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("bdd1@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("bdd1")


@when(u'User clicks on login button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[value='Login']").click()


@then(u'User should be logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "View your order history").is_displayed()


@when(u'User enters wrong credentials')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("bdd1")
    context.driver.find_element(By.ID, "input-password").send_keys("bdd1")


@then(u'Proper warning message should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                       "//*[text()='Warning: No match for E-Mail Address and/or Password.']").is_displayed()
