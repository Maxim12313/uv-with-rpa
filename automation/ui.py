from automation.config import TIMEOUT

from RPA.Browser.Selenium import Selenium, WebElement
from selenium import webdriver

# ------------Public


# add other options from here
def connect_default(url: str) -> Selenium:
    browser = Selenium()
    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    browser.open_available_browser(url, options=options)
    browser.maximize_browser_window()
    return browser


def producer_get_text_data(browser: Selenium) -> None:
    data_elements = wait_get(browser, "id:data")

    data = data_elements.text

    # get lines
    data = data.split("\n")

    # get individual words per line
    data = [line.split(" | ") for line in data]

    return data


def consumer_write_elements(
    browser: Selenium,
    name: str,
    power_level: str,
):
    form_element = wait_get(browser, "id:form")

    name_element = browser.find_element("name:name", form_element)
    power_level_element = browser.find_element("name:power_level", form_element)
    submit_element = browser.find_element("name:submit", form_element)

    write_element(name_element, name)
    write_element(power_level_element, power_level)
    submit_element.click()


# ------------Private Helpers


def write_element(element: WebElement, keys: str):
    element.clear()
    element.send_keys(keys)


def wait_get(browser: Selenium, locator: str):
    browser.wait_until_element_is_visible(locator, timeout=TIMEOUT)
    return browser.find_element(locator)
