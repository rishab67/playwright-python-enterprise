# 1. Import the 'expect' judge from playwright.sync_api
from playwright.sync_api import Playwright
from playwright.sync_api import expect


# 2. Define a test function named 'test_wikipedia_search' and pass it the '(page)' fixture
def test_wikipedia_search(page):
    print("Practice test")


# 3. Tell the page to goto "https://www.wikipedia.org/"
    page.goto("https://en.wikipedia.org")


# 4. Create a variable named 'search_box' and use page.get_by_placeholder() to find "Search Wikipedia"
    search_box = page.get_by_placeholder("Search Wikipedia").first
    expect(search_box).to_be_visible()
    expect(search_box).to_be_empty()

# 5. Tell the search_box to fill with the word "Python (programming language)"
    search_box.fill("Python (programming language)")


# 6. Tell the search_box to press "Enter"
    search_box.press("Enter")



# 7. Use the expect() judge on the (page) to_have_title "Python (programming language) - Wikipedia"

    expect(page).to_have_title("Python (programming language) - Wikipedia")