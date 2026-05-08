from playwright.sync_api import Playwright
from playwright.sync_api import expect
from pages.amazon_home_page import AmazonHomePage


def test_search_amazon_headphone(page):
    # 2. We "instantiate" (create) the Page Object and hand it the browser tab (page)
    home_page = AmazonHomePage(page)

    print("\n[Test 1] Opening Amazon India")
    # 3. We use the custom method from our Page Object instead of page.goto()
    home_page.navigate()

    # 4. We point the Judge at the search box variable stored inside the Page Object
    expect(home_page.search_box).to_be_visible()
    expect(home_page.search_box).to_be_empty()

    # 5. We use the custom method to search!
    home_page.search_for_item("Wireless Headphones")

    # 6. The final assertion stays exactly the same
    expect(page).to_have_title("Amazon.in : Wireless Headphones")


def test_search_amazon_shoes(page):
    home_page = AmazonHomePage(page)
    print("\n[Test 2] Opening Amazon India")
    home_page.navigate()

    expect(home_page.search_box).to_be_visible()
    expect(home_page.search_box).to_be_empty()

    home_page.search_for_item("Running Shoes")

    expect(page).to_have_title("Amazon.in : Running Shoes")