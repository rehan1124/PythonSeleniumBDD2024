from selenium import webdriver


def before_scenario(context, scenario):
    url = "https://tutorialsninja.com/demo/"
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.get(url)


def after_scenario(context, scenario):
    context.driver.quit()
