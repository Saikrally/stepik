from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"


with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        x = browser.find_element_by_id("input_value").text
        xvalue = calc(x)
        input1 = browser.find_element_by_id("answer").send_keys(xvalue)
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView();", button)
        checkbox = browser.find_element_by_css_selector('input[type="checkbox"]').click()
        radio = browser.find_element_by_css_selector('label[for="robotsRule"]').click()
        button.click()
    finally:
        time.sleep(5)
        browser.quit()
