from automation.ui import connect_default
from automation.config import URL
from robocorp.tasks import task


@task
def consume():
    browser = connect_default(URL + "/results")
    browser.close_window()
