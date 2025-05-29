from RPA.Browser.Selenium import Selenium
from robocorp.tasks import task


@task
def minimal_task():
    browser = Selenium()
    browser.open_available_browser("https://www.google.com")
    browser.input_text("name=q", "hello world")
    browser.press_keys("name=q", "ENTER")
    browser.wait_until_element_is_visible("id=search", timeout=10)
    browser.close_browser()
