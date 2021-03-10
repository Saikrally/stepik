from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
sel1 = "body > div > form > div.first_block > div.form-group.first_class > input"
sel2 = "body div > form > div.first_block > div.form-group.second_class > input"
sel3 = "body > div > form > div.first_block > div.form-group.third_class > input"


with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        input1 = browser.find_element_by_css_selector(sel1).send_keys("Firstname")
        input2 = browser.find_element_by_css_selector(sel2).send_keys("Lastname")
        input3 = browser.find_element_by_css_selector(sel3).send_keys("email@email.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)
        assert "Congratulations! You have successfully registered!" == browser.find_element_by_tag_name("h1").text

    finally:
        time.sleep(10)
        browser.quit()
