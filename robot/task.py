from robocorp.tasks import task
from RPA.Browser.Selenium import Selenium


@task
def task1():
    print("hello world")


@task
def task2():
    print("hello venus")


@task
def task3():
    print("hello jupiter")


@task
def task4():
    print("hello earth")
