class AmazonHomePage:

    # The __init__ method runs automatically when the Class is called.
    # This is where we store our locators!
    def __init__(self, page):
        self.page = page

        # 1. Create a class variable named 'self.search_box'
        self.search_box = page.get_by_placeholder("Search Amazon.in")

    # This is a Custom Method to handle navigation and security bypass
    def navigate(self):
        # 1. Go to the website
        self.page.goto("https://www.amazon.in")

        # 2. The Conditional Bypass (Your Idea)
        try:
            # Give the robot exactly 3000 milliseconds (3 seconds) to find and click the button.
            self.page.locator("text=Continue shopping").click(timeout=3000)
            print("\n[🛡️] Amazon Dog detected! Clicked 'Continue shopping' to bypass.")
        except Exception:
            # If 3 seconds pass and the button isn't there, ignore the error and proceed normally.
            pass

    # This is a Custom Method to handle the searching action
    def search_for_item(self, item_name):
        # 3. Tell self.search_box to fill with the dynamic variable: item_name
        self.search_box.fill(item_name)

        # 4. Tell self.search_box to press "Enter"
        self.search_box.press("Enter")