from selenium import webdriver
import math
import time

def open_page(www):
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get(www)
    time.sleep(1)
    return driver

if __name__=="__main__":
    browser = open_page("http://SunInJuly.github.io/execute_script.html")

    x = browser.find_element_by_id("input_value")
    x=int(x.text)
    print(x)
    rez = math.log(abs(12*(math.sin(x))))
    rez= str(rez)
    textbox=browser.find_element_by_id("answer")
    textbox.send_keys(rez)
    cbx= browser.find_element_by_id("robotCheckbox")
    cbx.click()
    btn = browser.find_element_by_class_name("btn-primary")

    scr="return arguments[0].scrollIntoView(true);"
    browser.execute_script(scr, btn)


    rb= browser.find_element_by_id('robotsRule') 
    rb.click()


    btn.click()
    time.sleep(5)
    browser.quit()

