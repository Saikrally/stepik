import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_item_to_cart(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert browser.find_element_by_css_selector("#add_to_basket_form > button").is_displayed(), "Basket isn't displayed"
