from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BOOKNAME_ADDED_TO_CART = (By.TAG_NAME, "h1")
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ADDED_PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    CART_MESSAGE_BOOKNAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    CART_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/text()")
    PRICE_ADDING_TO_CART = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    CART_PRODUCT_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")