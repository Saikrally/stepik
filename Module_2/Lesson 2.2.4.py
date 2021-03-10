from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    try:
        browser.get(link)
        first_name = browser.find_element_by_name("firstname").send_keys("First name")
        last_name = browser.find_element_by_name("lastname").send_keys("Last name")
        email = browser.find_element_by_name("email").send_keys("Email")
        current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего
        # исполняемого файла
        file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
        choose_file = browser.find_element_by_id("file").send_keys(file_path)
        submit_button_click = browser.find_element_by_class_name("btn.btn-primary").click()
    finally:
        time.sleep(15)
        browser.quit()
