from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User navigates to app home-page')
def step_impl(context):
    url = "https://tutorialsninja.com/demo/"
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()
    context.driver.get(url)


@when(u'User enters product in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'User enters invalid product in search box')
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


@when(u'User enters nothing in search box')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")


@then(u'User closes the browser')
def step_impl(context):
    context.driver.quit()
