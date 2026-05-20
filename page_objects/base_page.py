class BasePage:
    def __init__(self, page):
        # We inject Playwright's browser 'page' engine here
        self.page = page

    # We wrap Playwright's native commands in our own custom methods
    def navigate(self, url):
        self.page.goto(url)

    def click_element(self, selector):
        self.page.locator(selector).click()

    def fill_text(self, selector, text):
        self.page.locator(selector).fill(text)

