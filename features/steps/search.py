from behave import *

from features.pages.homepage import Homepage
from features.pages.searchpage import Searchpage


@given(u'User enters product in search box')
def step_impl(context):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name("HP")


@given(u'User enters invalid product in search box')
def step_impl(context):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name("JALALALALA")


@when(u'User clicks on search button')
def step_impl(context):
    context.home_page.click_search_button()


@then(u'Product should be displayed in search results')
def step_impl(context):
    context.search_page = Searchpage(context.driver)
    context.search_page.is_product_displayed("HP LP3065")


@then(u'Proper message for product not found should be displayed')
def step_impl(context):
    context.search_page = Searchpage(context.driver)
    context.search_page.is_invalid_product("There is no product that matches the search criteria.")


@given(u'User enters nothing in search box')
def step_impl(context):
    context.home_page = Homepage(context.driver)
    context.home_page.enter_product_name("")
