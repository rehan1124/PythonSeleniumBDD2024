from behave import *
from selenium.webdriver.common.by import By


@given(u'User enters product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@given(u'User enters invalid product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("JALALALALA")


@when(u'User clicks on search button')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id='search'] button").click()


@then(u'Product should be displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()


@then(u'Proper message for product not found should be displayed')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,
                                       "//p[text()='There is no product that matches the search criteria.']").is_displayed()


@given(u'User enters nothing in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")
