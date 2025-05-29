from RPA.Browser.Selenium import Selenium
from selenium import webdriver
from robocorp.tasks import task


@task
def minimal_task():
    browser = Selenium()

    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    browser.open_available_browser("", options=options)
    browser.maximize_browser_window()

    browser.input_text("name=q", "hello world")
    browser.press_keys("name=q", "ENTER")
    browser.wait_until_element_is_visible("id=search", timeout=10)
    browser.close_browser()
