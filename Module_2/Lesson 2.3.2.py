from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"


with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        button_click = browser.find_element_by_tag_name("button").click()
        first_window = browser.window_handles[0]
        new_window = browser.window_handles[1]
        new_window_go = browser.switch_to.window(new_window)
        x = calc(browser.find_element_by_id("input_value").text)
        input1 = browser.find_element_by_id("answer").send_keys(x)
        submit_button = browser.find_element_by_tag_name("button").click()

    finally:
        time.sleep(15)
        browser.quit()
