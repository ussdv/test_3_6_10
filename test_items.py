from selenium.webdriver.common.by import By
from time import sleep #for check
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_items(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    sleep(5) #for check
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")