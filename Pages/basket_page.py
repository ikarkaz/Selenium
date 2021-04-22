from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math, time
from .locators import AddToCardLocators

class BasketPage(BasePage):       
    def check_price(self, price):
      assert self.browser.find_element(*AddToCardLocators.BASKET_PRICE).text.strip() == price, 'Price: '+ price +";" +self.browser.find_element(*AddToCardLocators.BASKET_PRICE).text.strip()
      return True

    def check_goods(self, name):
        try:
            assert self.browser.find_element(*AddToCardLocators.BASKET_NAME).text.strip() == name, 'Name: '+ name +";" +self.browser.find_element(*AddToCardLocators.BASKET_NAME).text.strip()
        except Exception as ex:
            with open("log.txt", 'w+t', encoding='utf-8') as log:
                log.write(str(ex))
                raise ex
        return True
        
    def element_not_found (self):
        #отрицательная проверка
        pass