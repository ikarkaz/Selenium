from .base_page import BasePage
from .basket_page import BasketPage
from selenium.common.exceptions import NoAlertPresentException
import math, time
from .locators import AddToCardLocators

class AddToCard(BasePage):
    price = 0
    name = ''
    def check_buy (self):
        basket_page = self.click_btn()
        return (basket_page.check_goods(self.name) and basket_page.check_price(self.price))

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
    
    def alert_check(self, what, *locator):
        assert self.browser.find_element(locator[0], locator[1]).text.strip() == what, "AllertError: "  + what
        return True

    def click_btn(self):
        self.price = self.browser.find_element(*AddToCardLocators.PRICE).text.strip()
        self.name = self.browser.find_element(*AddToCardLocators.NAME).text.strip()
        btn= self.browser.find_element(*AddToCardLocators.ADD_TO_CARD_BTN)
        btn.click()
        self.solve_quiz_and_get_code()
        self.alert_check(self.name, *AddToCardLocators.Allert_Name)
        self.alert_check(self.price, *AddToCardLocators.Allert_price)
        self.browser.find_element(*AddToCardLocators.BASCET_BTN).click()
        return BasketPage(self.browser, self.browser.current_url)

    def should_not_be_success_message(self, *locator):
        assert self.is_not_element_present(locator), \
            "Success message is presented, but should not be"