import time
from selenium import webdriver
from selenium.webdriver.support import select

def open_page(www):
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get(www)
    time.sleep(1)
    return driver

driver =open_page("http://suninjuly.github.io/selects1.html")
x = driver.find_element_by_css_selector(".nowrap#num1")
x=int(x.text)
print(x)
y = driver.find_element_by_css_selector(".nowrap#num2")
y=int(y.text)
print(y)
rez = x+y
# Напишем текст ответа в найденное поле

select = select.Select(driver.find_element_by_id('dropdown'))
select.select_by_value(str(rez))
submit_button = driver.find_element_by_css_selector(".btn-default")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
