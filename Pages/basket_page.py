from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math, time
from .locators import AddToCardLocators

class BasketPage(BasePage):       
    def check_goods(self):
        # Ждем появления аллертов.
        #Получаем все элементы. В 1 элементе проверяем имя книги с .... надо считать имя книги заранее, во вторм цену .. так же надо считать цену заранее
        return True
    def check_price(self):
        return True

    def element_not_found (self):
        #отрицательная проверка
        pass