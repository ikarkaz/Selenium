from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BTN = (By.NAME, "login_submit")
    REGISTR_FORM = (By.CSS_SELECTOR,"#register_form")
    REGISTR_BTN = (By.NAME, "registration_submit")

class AddToCardLocators():
    ADD_TO_CARD_BTN = (By.CSS_SELECTOR,".btn-add-to-basket")
    BASKET_NAME = (By.CSS_SELECTOR,"#basket_formset > div > div > div.col-sm-4 > h3 > a")
    BASKET_PRICE = (By.CSS_SELECTOR,"#basket_formset > div > div > div:nth-child(5) > p")
    NAME = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    BASCET_BTN = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    Allert_Name = (By.CSS_SELECTOR,'#messages > div:nth-child(1) > div > strong')
    Allert_price = (By.CSS_SELECTOR,'#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
