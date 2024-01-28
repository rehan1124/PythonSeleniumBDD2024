from behave import *

from features.pages.homepage import Homepage
from features.pages.searchpage import Searchpage


@given(u'User enters product "{product_name}" in search box')
def step_impl(context, product_name):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name(product_name)


@given(u'User enters invalid product "{product_name}" in search box')
def step_impl(context, product_name):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name(product_name)


@when(u'User clicks on search button')
def step_impl(context):
    context.home_page.click_search_button()


@then(u'Product "{product_name}" should be displayed in search results')
def step_impl(context, product_name):
    context.search_page = Searchpage(context.driver)
    context.search_page.is_product_displayed(product_name)


@then(u'Message for product not found should be displayed "{message}"')
def step_impl(context, message):
    context.search_page = Searchpage(context.driver)
    context.search_page.is_invalid_product(message)


@given(u'User enters nothing in search box')
def step_impl(context):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name("")
