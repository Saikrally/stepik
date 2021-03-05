from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"


with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        x_element = browser.find_element_by_id("input_value")
        x = x_element.text
        y = calc(x)
        input1 = browser.find_element_by_id("answer")
        input1.send_keys(y)
        checkbox = browser.find_element_by_css_selector('input[type="checkbox"]')
        checkbox.click()
        radio = browser.find_element_by_css_selector('label[for="robotsRule"]')
        radio.click()
        button = browser.find_element_by_class_name("btn.btn-default")
        #button.click()

    finally:
        time.sleep(10)
        browser.quit()
