from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return x + y


link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        x = int(browser.find_element_by_id("num1").text)
        y = int(browser.find_element_by_id("num2").text)
        sum = str(calc(x, y))
        select = Select(browser.find_element_by_tag_name("select"))
        select.select_by_value(sum)
        button = browser.find_element_by_css_selector("body > div > form > button").click()
    finally:
        time.sleep(5)
        browser.quit()
