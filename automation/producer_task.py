# mine
from automation.config import URL
import automation.ui as ui

# third party
from robocorp.tasks import task
from robocorp import workitems


@task
def produce():
    browser = ui.connect_default(URL + "/reader")
    data = ui.producer_get_text_data(browser)
    for line in data:
        output = {"name": line[0], "age": line[1], "is_cool": line[2]}
        workitems.outputs.create(output)

    browser.close_window()
