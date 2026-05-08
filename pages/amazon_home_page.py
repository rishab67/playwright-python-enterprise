class AmazonHomePage:

    #The __init__ method runs automatically when the Class is called.
    # This where we store our locators!
    def __init__(self, page):
        self.page = page

        # --- YOUR PSEUDOCODE CHALLENGE STARTS HERE ---



        # 1. Create a class variable named 'self.search_box' and assign it the Amazon search box locator.
        # (Hint: use page.get_by_placeholder just like before)
        self.search_box = page.get_by_placeholder("Search Amazon.in")



        # This is a Custom Method to handle navigation
        # 2. Tell self.page to goto the Amazon India URL
    def navigate(self):
        self.page.goto("https://www.amazon.in")


        # This is a Custom Method to handle the searching action
    def search_for_item(self, item_name):
        self.search_box.fill(item_name)

    # 3. Tell self.search_box to fill with the dynamic variable: item_name

    # 4. Tell self.search_box to press "Enter"
        self.search_box.press("Enter")