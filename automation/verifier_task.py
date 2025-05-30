from automation.ui import connect_default
from automation.config import URL
from robocorp.tasks import task

# NOTE: something extra reading the results page for cicd testing?


@task
def consume():
    browser = connect_default(URL + "/results")
    browser.close_window()
