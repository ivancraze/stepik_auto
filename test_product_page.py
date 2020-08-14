from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time
import pytest

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	# time.sleep(120)
	page.should_be_add_message()
	page.should_be_book_name()
	page.should_be_book_price()

# @pytest.mark.parametrize("link", [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
# def test_guest_can_add_product_to_basket(browser, link):
# 	link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_to_basket()
# 	page.solve_quiz_and_get_code()
# 	page.should_be_add_message()
# 	page.should_be_book_name()
# 	page.should_be_book_price()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_to_basket()
# 	page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 	page = ProductPage(browser, link)
# 	page.open()
# 	page.add_to_basket()
# 	page.success_message_should_be_disappeared()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):    
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"    
    page = ProductPage(browser, link)    
    page.open()    
    page.go_to_login_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "111222333"
        page.register_new_user(self, email, password)
		
    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_message_success()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_basket_button()
        page.add_to_basket()
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()