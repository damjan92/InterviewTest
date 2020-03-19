import pytest
from base.webdriver_factory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method Level setUp")
    yield
    print("Running method level tearDown")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("## Running oneTime level setUp")

    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstantce()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("## Running oneTime level tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operation system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return  request.config.getoption("--osType")
