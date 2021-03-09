from selenium import webdriver
import time
import unittest
import pytest


class TestLink(unittest.TestCase):

    def test_link1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > "
            "input")
        input1.send_keys("Firstname")
        input2 = browser.find_element_by_css_selector(
            "body div > form > div.first_block > div.form-group.second_class > "
            "input")
        input2.send_keys("Lastname")
        input3 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > "
            "input")
        input3.send_keys("email@email.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal")

    def test_link2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.first_class > "
            "input")
        input1.send_keys("Firstname")
        input2 = browser.find_element_by_css_selector(
            "body div > form > div.first_block > div.form-group.second_class > "
            "input")
        input2.send_keys("Lastname")
        input3 = browser.find_element_by_css_selector(
            "body > div > form > div.first_block > div.form-group.third_class > "
            "input")
        input3.send_keys("email@email.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(2)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be equal")


if __name__ == "__main__":
    unittest.main()
