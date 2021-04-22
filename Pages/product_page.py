from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
import math, time
from .locators import AddToCardLocators

class AddToCard(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def click_btn(self):
        price = self.browser.find_element(*AddToCardLocators.PRICE).text.strip()
        name = self.browser.find_element(*AddToCardLocators.NAME).text.strip()
        btn= self.browser.find_element(*AddToCardLocators.ADD_TO_CARD_BTN)
        time.sleep(4)
        btn.click()
        self.solve_quiz_and_get_code()
        self.browser.find_element(*AddToCardLocators.BASCET_BTN).click()
        return 
        
    def check_price(self, price):
      assert self.browser.find_element(*AddToCardLocators.BASKET_PRICE).text.strip() == price, 'Price: '+ price +";" +self.browser.find_element(*AddToCardLocators.BASKET_PRICE).text.strip()
    def check_goods(self, name):
        try:
            assert self.browser.find_element(*AddToCardLocators.BASKET_NAME).text.strip() == name, 'Name: '+ name +";" +self.browser.find_element(*AddToCardLocators.BASKET_NAME).text.strip()
        except Exception as ex:
            with open("log.txt", 'w+t', encoding='utf-8') as log:
                log.write(str(ex))
                raise ex