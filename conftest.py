import pytest
from playwright.sync_api import sync_playwright
from api_clients.booking_client import BookingClient
from core.config import Config

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }


@pytest.fixture
def booking_manager(playwright):
    # ====== THE SETUP PHASE ======
    # 1. Properly boot up Playwright's blazing-fast API engine
    request_context = playwright.request.new_context()

    # 2. Hand the engine to our API Client
    client = BookingClient(request_context)
    created_booking_ids = []  # Empty list to track the trash

    # The 'yield' pauses this file and hands the tools over to the test
    yield client, created_booking_ids

    # ====== THE TEARDOWN PHASE ======
    # This executes AFTER the test finishes!
    if created_booking_ids:
        print("\n[🗑️] Global Manager initiated auto-cleanup...")

        # Get the Admin Token once using our active request context
        auth_response = request_context.post(
            f"{Config.API_BASE_URL}/auth",
            data={
                "username": Config.ADMIN_USERNAME,
                "password": Config.ADMIN_PASSWORD
            }
        )
        token = auth_response.json()["token"]

        # Loop through every piece of trash in the list and destroy it
        for b_id in created_booking_ids:
            client.delete_booking(b_id, token)
            print(f"[-] Auto-deleted Booking ID: {b_id}")

    # 3. Cleanly shut down the Playwright engine
    request_context.dispose()