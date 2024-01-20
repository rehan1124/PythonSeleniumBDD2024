from behave import *

from features.pages.accountloginpage import Accountloginpage
from features.pages.myaccountpage import Myaccountpage
from features.pages.searchpage import Searchpage


@given(u'User navigates to login page')
def step_impl(context):
    search_page = Searchpage(context.driver)
    search_page.click_my_account()
    search_page.click_login_link()


@when(u'User enters credentials')
def step_impl(context):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.enter_email_address("bdd1@gmail.com")
    account_login_page.enter_password("bdd1")


@when(u'User clicks on login button')
def step_impl(context):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.click_login_button()


@then(u'User should be logged in')
def step_impl(context):
    my_account_page = Myaccountpage(context.driver)
    my_account_page.is_user_logged_in("View your order history")


@when(u'User enters wrong credentials')
def step_impl(context):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.enter_email_address("bdd1")
    account_login_page.enter_password("bdd1")


@then(u'Proper warning message should be displayed')
def step_impl(context):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.is_warning_message_displayed("Warning: No match for E-Mail Address and/or Password.")
