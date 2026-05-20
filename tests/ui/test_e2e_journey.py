#import pytest
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage



#@pytest.mark.xfail(reason ="Intentionally failing to study the HTML report ")
def test_end_to_end_shopping_journey(page):
    # 1. Initialize our Page Objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 2. Execute the Login Journey
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # 3. Execute the Inventory Journey
    inventory_page.add_backpack_to_cart()

    # 4. Extract and Assert the UI State
    cart_count = inventory_page.get_cart_count()

    # 5. Mathematically prove the UI worked
    assert cart_count == "1"

    print(f"\n[+] E2E SUCCESS: Backpack added! Cart count is proven to be: {cart_count}")

