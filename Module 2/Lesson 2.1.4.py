from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        people_radio = browser.find_element_by_id("peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked == "false"

    finally:
        time.sleep(1)
        browser.quit()
