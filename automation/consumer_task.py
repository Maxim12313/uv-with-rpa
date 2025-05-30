# mine
import automation.ui as ui
from automation.config import URL

# 3rd party
from robocorp import workitems
from robocorp.tasks import task


def validate(payload: dict):
    return str(payload["name"]), int(payload["age"]), bool(payload["is_cool"])


@task
def consume():
    browser = ui.connect_default(URL + "/writer")

    for item in workitems.inputs:
        payload = item.payload
        try:
            name, age, is_cool = validate(payload)
            power_level = age if not is_cool else age * age
            ui.consumer_write_elements(browser, name, power_level)
        except Exception:
            print("failed")

    browser.close_window()
