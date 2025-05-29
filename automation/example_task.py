from robocorp.tasks import task
from automation.ui import connect_default


@task
def default_task():
    browser = connect_default("https://www.google.com")

    browser.input_text("name=q", "hello world")
    browser.press_keys("name=q", "ENTER")
    browser.wait_until_element_is_visible("id=search", timeout=10)

    browser.close_browser()
