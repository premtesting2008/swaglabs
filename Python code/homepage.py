from locators.locators import Locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.product_add_to_cart_xpath = Locators.product_add_to_cart_xpath
        self.cart_xpath = Locators.cart_xpath

    def add_to_cart(self):
        self.driver.find_element_by_xpath(self.product_add_to_cart_xpath).click()
        self.driver.find_element_by_xpath(self.cart_xpath).click()

    def click_cart(self):
        self.driver.find_element_by_xpath(self.cart_xpath).click()