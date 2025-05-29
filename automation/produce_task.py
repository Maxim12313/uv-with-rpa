from RPA.Browser.Selenium import Selenium
from selenium import webdriver
from robocorp.tasks import task


@task
def produce():
    print("producing")
