import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.set_window_size(1366, 768)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.tempspins.pw/en")
time.sleep(5)
