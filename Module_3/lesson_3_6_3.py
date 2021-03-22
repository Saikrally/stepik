import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAnswerPage:

    def test_answer_check(self, browser):
        answer = math.log(int(time.time()))
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector("textarea").send_keys(str(answer))

