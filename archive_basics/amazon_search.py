from playwright.sync_api import sync_playwright

#1. We added a new parameter called "item_to_search"
def search_amazon(playwright,item_to_search):
    #2.Open browser
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()


    #3. Go to Amazon India
    print("Opening Amazon India...")
    page.goto("https://www.amazon.in/")
    #page.wait_for_timeout(3000)

    #4. The f-string lets us print exactly what is inside our variable
    print(f"Searching for {item_to_search}...")


    #5. Find the search box, type into it and press Enter. For that we preferred to use "Modern" locator method!
    #search_box = page.locator("#twotabsearchtextbox")
    search_box = page.get_by_placeholder("Search Amazon.in")


    #6. Instead of hardcoding text, we tell it to fill the box with our variable
    search_box.fill(item_to_search)
    search_box.press("Enter")


    #7. Pause for 5 sec so we can the ui search result
    print("Waiting for the search result to appear...")
    page.wait_for_timeout(5000)


    #8. Print the tittle of the new result page
    print(f"The new page title is  {page.title()}")


    #9. Close up
    browser.close()


with sync_playwright() as p:
    #now we can easily change the search term right here at the starting line!
    search_amazon(p, "Wireless Headphones")

    # We could even run it a second time immediately after with a different item!
    search_amazon(p, "Running Shoes")
