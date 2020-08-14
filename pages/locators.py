from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
	BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group a.btn")

class LoginPageLocators():
	LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
	REG_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
	REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
	REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators:
	ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
	ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
	BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
	MESSAGE_BASKET_ALL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

class BasketPageLocators:
	MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
	ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")