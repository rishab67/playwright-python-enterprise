from page_objects.base_page import BasePage


# Notice how LoginPage has (BasePage) in parentheses? That is INHERITANCE.
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)  # This special command wakes up the BasePage parent
        self.url = "https://www.saucedemo.com/"

        # Locators: We hide these inside the class (Encapsulation)
        self.username_input = "[data-test='username']"
        self.password_input = "[data-test='password']"
        self.login_button = "[data-test='login-button']"

    def load(self):
        # We are using the navigate() method we inherited from the parent!
        self.navigate(self.url)

    def login(self, username, password):
        # We are using the fill_text() and click_element() methods from the parent!
        self.fill_text(self.username_input, username)
        self.fill_text(self.password_input, password)
        self.click_element(self.login_button)