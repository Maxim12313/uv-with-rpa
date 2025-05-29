from automation.config import URL
from automation.ui import connect_default

from robocorp.tasks import task
from robocorp import workitems


@task
def produce():
    browser = connect_default(URL + "/reader")
    browser.close_window()
