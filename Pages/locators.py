from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BTN = (By.NAME, "login_submit")
    REGISTR_FORM = (By.CSS_SELECTOR,"#register_form")
    REGISTR_BTN = (By.NAME, "registration_submit")

class AddToCardLocators():
    ADD_TO_CARD_BTN = (By.CSS_SELECTOR ,".btn-add-to-basket")
    ALLERT_1 = ("alertinner")
    ALLERT_3 = (".alertinner strong")
    NAME = (".product_main")
    PRICE = (".price_color")
    BASCET_BTN = (".btn btn-default")