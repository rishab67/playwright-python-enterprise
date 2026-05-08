from playwright.sync_api import sync_playwright


def run_automation(playwright):
    # launch the chromium in headed mode so that we can see the browser in the ui mode
    browser = playwright.chromium.launch(headless = False)
    page = browser.new_page()

    #navigate to the website
    print("Navigating to the website...")
    page.goto("https://www.amazon.in/?tag=indiatimes3-21&gad_source=1")
    page.wait_for_timeout(3000) # This tell the robot to freeze it for 3 sec

    #Extract and print the tittle of the page
    print(f"The title of the page is {page.title()}")

    #close the browser
    browser.close()

# this is the entry point that start the Playwright context
with sync_playwright() as p:
    run_automation(p)
