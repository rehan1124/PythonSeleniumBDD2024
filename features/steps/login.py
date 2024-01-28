from behave import *

from features.pages.accountloginpage import Accountloginpage
from features.pages.myaccountpage import Myaccountpage
from features.pages.searchpage import Searchpage


@given(u'User navigates to login page')
def step_impl(context):
    search_page = Searchpage(context.driver)
    search_page.click_my_account()
    search_page.click_login_link()


@when(u'User enters credentials "{email}" "{password}"')
def step_impl(context, email, password):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.enter_email_address(email)
    account_login_page.enter_password(password)


@when(u'User clicks on login button')
def step_impl(context):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.click_login_button()


@then(u'User should be logged in and see link "{text}"')
def step_impl(context, text):
    my_account_page = Myaccountpage(context.driver)
    my_account_page.is_user_logged_in(text)


@when(u'User enters wrong credentials "{email}" "{password}"')
def step_impl(context, email, password):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.enter_email_address(email)
    account_login_page.enter_password(password)


@then(u'Proper warning message "{message}" should be displayed')
def step_impl(context, message):
    account_login_page = Accountloginpage(context.driver)
    account_login_page.is_warning_message_displayed(message)
