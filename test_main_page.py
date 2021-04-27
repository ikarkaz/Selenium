from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    link = "http://selenium1py.pythonanywhere.com/"
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage(browser, self.link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open() # открываем страницу
        page.go_to_login_page()                      
        login_page =  LoginPage (browser, browser.current_url)         # выполняем метод страницы — переходим на страницу логина
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, self.link)
        page.open()
        page.browser.find_element_by_css_selector("#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a").click()
        page.basket_is_empty()

