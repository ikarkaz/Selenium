from .Pages.product_page import AddToCard
from .Pages.locators import AddToCardLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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

@pytest.mark.negativ
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    #Не стал я это все реализовывать в соответсвующем классе, все равно проект заканчивается
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddToCard(browser, link)
    page.open()
    page.browser.find_element_by_css_selector("#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a").click()
    allert_text = {'en': "Your basket is empty.", "ru": "Ваша корзина пуста"}
    assert WebDriverWait(page.browser, 5).until_not(EC.presence_of_element_located((By.ID, "basket-items")))
    assert WebDriverWait(page.browser, 5).until(EC.text_to_be_present_in_element((By.ID, 'content_inner'), allert_text['en']))

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddToCard(browser, link)
    page.open()
    page.should_not_be_success_message( )

@pytest.mark.negativ
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddToCard(browser, link)
    page.open()
    page.guest_cant_see_success_message_after_adding_product_to_basket()

def test_message_disappeared_after_adding_product_to_basket():
    """Открываем страницу товара
Добавляем товар в корзину
Проверяем, что нет сообщения об успехе с помощью is_disappeared"""
    pass
