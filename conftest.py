import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='http://192.168.0.93:8081')


@pytest.fixture(scope='session')
def base_url(request):
    yield request.config.getoption('--url')


@pytest.fixture(scope='session')
def driver(request):
    browser_name = request.config.getoption('--browser')

    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    elif browser_name == 'safari':
        browser = webdriver.Safari()
    else:
        raise ValueError('Unknown browser')

    yield browser

    browser.close()
