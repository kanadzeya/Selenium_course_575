from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): # Наследование обязательно!
    def add_to_cart_click(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_product_adding_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_MESSAGE_BOOKNAME), "Message not found"

    def product_in_basket_is_the_same(self):
        # Обязательно .text для сравнения строк
        added_book = self.browser.find_element(*ProductPageLocators.CART_MESSAGE_BOOKNAME).text
        book_in_cart = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert added_book == book_in_cart, f"Expected {added_book}, got {book_in_cart}"

    def price_in_basket_is_the_same(self):
        added_price = self.browser.find_element(*ProductPageLocators.PRICE_ADDING_TO_CART).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE).text
        assert added_price == price_in_cart, f"Expected {added_price}, got {price_in_cart}"
