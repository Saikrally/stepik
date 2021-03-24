import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @pytest.mark.parametrize('siteid', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_answer_check(self, browser, siteid):
        printed_text = ""
        answer = math.log(int(time.time()))
        link = f"https://stepik.org/lesson/{siteid}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)
        browser.find_element_by_css_selector("textarea").send_keys(str(answer))
        submit_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        submit_button.click()
        correct_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
        if correct_text != "Correct":
            printed_text += correct_text.text
            print(printed_text)
        assert correct_text.text == "Correct!", "Should be 'Correct' in correct_text variable"

