from selenium import webdriver
import execute2_js
import time
import os.path

def text_input (brow,name, text):
    browser = brow
    element = browser.find_element_by_name(name)
    element.send_keys(text)
def btn_click( brow,css):
    browser = brow
    element = browser.find_element_by_css_selector(css)
    element.click()

if __name__=="__main__":
    www = r"http://suninjuly.github.io/file_input.html"
    browser = execute2_js.open_page(www)
    first = text_input(browser, "firstname", "P")

    Last = text_input(browser, "lastname", "K")

    email =text_input(browser, "email", "i@m.ru")

    file_path = os.path.join(os.path.abspath(os.path.curdir), "test.txt")
    file = text_input(browser, "file", file_path)

    submit = btn_click(browser, ".btn")