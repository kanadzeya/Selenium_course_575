from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_to_cart_click(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        self.browser.execute_script("arguments[0].click();", button)

    def should_be_product_adding_message(self):
        # Ждем, пока сообщение действительно появится в DOM
        assert WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.CART_MESSAGE_BOOKNAME)
        ), "Success message is not presented"

    def product_in_basket_is_the_same(self):
        message_book = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(ProductPageLocators.CART_MESSAGE_BOOKNAME)
        ).text
        product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert message_book == product_name, f"Ожидали {product_name}, получили {message_book}"

    def price_in_basket_is_the_same(self):
        added_price = self.browser.find_element(*ProductPageLocators.PRICE_ADDING_TO_CART).text
        price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_PRICE).text
        assert added_price == price_in_cart, f"Expected {added_price}, got {price_in_cart}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CART_MESSAGE_BOOKNAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.CART_MESSAGE_BOOKNAME), \
            "Success message did not disappear"