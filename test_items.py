import selenium

def test_change_btn_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    brw = browser
    brw.get(link)
    assert brw.find_element_by_css_selector("#add_to_basket_form >button.btn-add-to-basket"), "btn not found"