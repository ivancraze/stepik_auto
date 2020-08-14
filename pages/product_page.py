from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_to_basket(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "No add to basket button"
		basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
		basket_button.click()

	def should_be_add_message(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "No success message"

	def should_be_book_name(self):
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
		print(product_name, message)
		assert message == product_name, f"{product_name} is not {message}"

	def should_be_add_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

	def should_be_book_price(self):
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
		print(product_price, basket_price)
		assert product_price == basket_price, f"{product_price} not equal {basket_price}"

	def should_be_message_about_adding(self):
		assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Message about adding is not presented"
		product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
		assert product_name == message, "No product name in the message or wrong name"

	def should_be_message_basket_total(self):
		assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_ALL), "Message basket total is not presented"
		assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
		message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_ALL).text
		product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
		assert product_price in message_basket_total, "No product price in the message"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"

	def success_message_should_be_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), "Success message is presented, but should not be"