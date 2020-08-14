from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def add_to_basket(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'No add to basket button'
		basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		basket_button.click()

	def should_be_add_message(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), 'No success message'

	def should_be_book_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
		print(product_name, message)
		assert message == product_name, f"{product_name} is not {message}"

	def should_be_book_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		print(product_price, basket_price)
		assert product_price == basket_price, f"{product_price} not equal {basket_price}"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"

	def success_message_should_be_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"