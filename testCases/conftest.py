import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request): # this will return the browser value to the setup method
    return request.config.getoption('--browser')

# pytest HTML reports
def pytest_html_report_title(report):
    report.title = "Test Execution Report (OpenCart)"

def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "OpenCart"
    config.stash[metadata_key]["Module"] = "--"
    config.stash[metadata_key]["Tester"] = "Silas Francis"

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)
    metadata.pop('Platform', None)



