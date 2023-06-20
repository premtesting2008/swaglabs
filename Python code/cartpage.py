from locators.locators import Locators


class CartPage():
    def __init__(self, driver):
        self.driver = driver

        self.checkout_button_xpath = Locators.checkout_button_xpath

        self.fname_id = Locators.fname_id
        self.lname_id = Locators.lname_id
        self.zip_id = Locators.zip_id

        self.continue_button_id = Locators.continue_button_id
        self.finish_button_id = Locators.finish_button_id

    def click_checkout(self):
        self.driver.find_element_by_xpath(self.checkout_button_xpath).click()

    def enter_info(self, fname, lname, zip):
        self.driver.find_element_by_id(self.fname_id).send_keys(fname)
        self.driver.find_element_by_id(self.lname_id).send_keys(lname)
        self.driver.find_element_by_id(self.zip_id).send_keys(zip)

    def click_continue(self):
        self.driver.find_element_by_id(self.continue_button_id).click()

    def click_finish(self):
        self.driver.find_element_by_id(self.finish_button_id).click()
