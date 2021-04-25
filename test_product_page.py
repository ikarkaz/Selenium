from .Pages.product_page import AddToCard
from .Pages.locators import AddToCardLocators
import pytest


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_add_to_card (browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = AddToCard(browser, link)
    page.open()
    assert page.check_buy(), "BuyError"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToCard(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToCard(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает главную страницу
Переходит в корзину по кнопке в шапке сайта
Ожидаем, что в корзине нет товаров
Ожидаем, что есть текст о том что корзина пуста """
    pass

@pytest.mark.negativ
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToCard(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket():
    """
    Открываем страницу товара
Добавляем товар в корзину
Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    pass

def test_message_disappeared_after_adding_product_to_basket():
    """Открываем страницу товара
Добавляем товар в корзину
Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    pass
