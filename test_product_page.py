from .Pages.product_page import AddToCard


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_add_to_card (browser):
    page = AddToCard(browser, link)
    page.open()
    assert page.click_btn(), "Test not Good"