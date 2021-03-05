from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


# find_element_by_css_selector('input[type="checkbox"]')
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        chest = browser.find_element_by_id("treasure")
        valuex = chest.get_attribute("valuex")
        print(valuex)
        x = calc(valuex)
        print(x)
        text_field = browser.find_element_by_id("answer")
        text_field.send_keys(x)
        checkbox = browser.find_element_by_id("robotCheckbox")
        checkbox.click()
        radiobutton = browser.find_element_by_id("robotsRule")
        radiobutton.click()
        submit_button = browser.find_element_by_css_selector("body > div > form > div > div > button")
        submit_button.click()

    finally:
        time.sleep(5)
        browser.quit()
