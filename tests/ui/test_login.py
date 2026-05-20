from page_objects.login_page import LoginPage
from playwright.sync_api import expect


def test_valid_login(page):
    # 1. Wake up the LoginPage object
    login_page = LoginPage(page)

    # 2. Do the actions
    login_page.load()
    # Swag Labs has hardcoded dummy credentials for us to use
    login_page.login("standard_user", "secret_sauce")

    # 3. Assert: Mathematically prove the login worked
    # If login is successful, the website redirects to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("\n[+] SUCCESS: UI Login completely automated via Page Object Model!")