from selenium import webdriver
from utilities.config_reader import read_config


def before_scenario(context, scenario):
    app_url = read_config("DEFAULT", "URL")
    implicit_wait = read_config("DEFAULT", "IMPLICIT_WAIT")
    browser = read_config("DEFAULT", "BROWSER")
    if browser == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        context.driver = webdriver.Chrome(options=options)
    elif browser == "Firefox":
        # options = webdriver.FirefoxOptions()
        # options.add_argument('--no-sandbox')
        # context.driver = webdriver.Firefox(options=options)
        context.driver = webdriver.Firefox()
    elif browser == "Edge":
        options = webdriver.EdgeOptions()
        options.add_argument('--no-sandbox')
        context.driver = webdriver.Edge(options=options)
        context.driver = webdriver.Edge()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(implicit_wait)
    context.driver.get(app_url)


def after_scenario(context, scenario):
    context.driver.quit()
