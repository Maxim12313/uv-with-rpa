from RPA.Browser.Selenium import Selenium
from selenium import webdriver


# add other options from here
def connect_default(url: str) -> Selenium:
    browser = Selenium()
    options = webdriver.FirefoxOptions()
    options.add_argument("--private")
    browser.open_available_browser(url, options=options)
    browser.maximize_browser_window()
    return browser
