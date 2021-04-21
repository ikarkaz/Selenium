from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_BTN = (By.NAME, "login_submit")
    REGISTR_FORM = (By.CSS_SELECTOR,"#register_form")
    REGISTR_BTN = (By.NAME, "registration_submit")