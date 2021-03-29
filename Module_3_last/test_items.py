import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_item_to_cart(browser):
    browser.get(link)
    #time.sleep(30)
    is_element_present = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert is_element_present == browser.find_element_by_css_selector("#add_to_basket_form > button").is_displayed()

"""import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store',
                     default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'], )
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()"""