from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_click()
    page.solve_quiz_and_get_code()
    page.should_be_product_adding_message()
    page.product_in_basket_is_the_same()
    page.price_in_basket_is_the_same()