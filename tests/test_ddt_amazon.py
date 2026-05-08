import pytest
import csv
from playwright.sync_api import Playwright
from playwright.sync_api import expect
from pages.amazon_home_page import AmazonHomePage


# This helper function opens your csv and reads the data
def read_test_data():
    with open("data/search_data.csv",mode = "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        return list(csv_reader)


@pytest.mark.parametrize("search_term,expected_title",read_test_data())
def test_search_term(page,search_term,expected_title):
    # --- YOUR PSEUDOCODE CHALLENGE STARTS HERE ---

    # 1. Instantiate (create) the Page Object and hand it the (page) fixture.
    # Store it in a variable named 'home_page'.
    home_page = AmazonHomePage(page)



    # 2. Tell the home_page to navigate()
    home_page.navigate()

    # 3. Tell the strict Judge to check if the home_page's search_box is visible
    expect(home_page.search_box).to_be_visible()

    # 4. Tell the strict Judge to check if the home_page's search_box is empty
    expect(home_page.search_box).to_be_empty()


    # 5. Tell the home_page to search_for_item() using the dynamic variable: search_term
    home_page.search_for_item(search_term)


    # 6. Tell the Judge to check if the (page) has the title using the dynamic variable: expected_title
    expect(page).to_have_title(expected_title)