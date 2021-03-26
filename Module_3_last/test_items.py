import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
time.sleep(30)


def add_item_to_cart(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn btn-lg btn-primary btn-add-to-basket").click()
    assert browser.find_element_by_class_name("btn btn-lg btn-primary btn-add-to-basket")

