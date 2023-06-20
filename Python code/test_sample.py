import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.cartpage import CartPage


class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="C:/Users/abina/PycharmProjects/SeleniumProject/drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        print("test completed")

    def test_login(self, test_setup):
        driver.get("https://www.saucedemo.com/")
        login = LoginPage(driver)
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

        home = HomePage(driver)
        home.add_to_cart()
        home.click_cart()

        cart = CartPage(driver)
        cart.click_checkout()
        cart.enter_info("abc","xyz","560076")
        cart.click_continue()
        cart.click_finish()

