from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from selenium.webdriver.edge.service import Service as ServiceEdge
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        service_obj = ServiceChrome(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser == 'firefox':
        service_obj = ServiceFirefox(r"C:\Users\davud\Desktop\SeleniumD\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
    elif browser == 'edge':
        service_obj = ServiceEdge(r"C:\Users\davud\Desktop\SeleniumD\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
    else:
        service_obj = ServiceChrome(r"C:\Users\davud\Desktop\SeleniumD\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)

    return driver


def pytest_addoption(parser):  # this will get value from CLI / hooks
    parser.addoption("--browser")



@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")

    # **************** HTML report ******************

    # It is hook for adding environment info to HTML report


def pytest_configure(config):
    config._metadata['Project Name'] = 'DEMO QA'
    config._metadata['Module Name'] = 'QA'
    config._metadata['QA Engineer'] = 'Davud Gobeljic'

    # It is hook for delete/modify environment info to HTML report


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

