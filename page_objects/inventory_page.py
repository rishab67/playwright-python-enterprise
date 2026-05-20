from page_objects.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Locators: Encapsulated specific HTML addresses
        self.backpack_add_button = "[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_badge = ".shopping_cart_badge"

    def add_backpack_to_cart(self):
        # We inherit the click_element method from BasePage
        self.click_element(self.backpack_add_button)

    def get_cart_count(self):
        # We reach directly into the browser to extract the text from the red badge
        return self.page.locator(self.cart_badge).inner_text()