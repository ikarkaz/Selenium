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
        btn= self.browser.find_element(*AddToCardLocators.ADD_TO_CARD_BTN)
        btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(290)
        return True
        
    def check_goods(self):
        # Ждем появления аллертов.
        #Получаем все элементы. В 1 элементе проверяем имя книги с .... надо считать имя книги заранее, во вторм цену .. так же надо считать цену заранее
        return True
    def check_price(self):
        return True

