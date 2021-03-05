from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"


with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        button_submit = browser.find_element_by_tag_name("button").click()
        confirm = browser.switch_to.alert.accept()
        x = calc(browser.find_element_by_id("input_value").text)
        input1 = browser.find_element_by_id("answer").send_keys(x)
        submit = browser.find_element_by_xpath("/html/body/form/div/div/button").click()
    finally:
        time.sleep(15)
        browser.quit()
