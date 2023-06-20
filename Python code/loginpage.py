from locators.locators import Locators


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_name = Locators.password_textbox_name
        self.button_id = Locators.button_id

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.button_id).click()
