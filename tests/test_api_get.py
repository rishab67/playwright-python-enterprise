# 1. Import the 'expect' judge from playwright.sync_api
from playwright.sync_api import expect


# 2. Define a test function named 'test_get_user_data'.
# CRITICAL DIFFERENCE: Instead of passing it the '(page)' fixture, pass it the '(request)' fixture.
def test_get_user_data(page):
    response = page.request.get("https://jsonplaceholder.typicode.com/users/1")
    json_data = response.json()

    print(json_data)
    print(response.status)
    expect(response).to_be_ok()


    assert json_data["name"] == "Leanne Graham"




    # 3. Tell the 'request' fixture to perform a .get() action on this exact URL: "https://jsonplaceholder.typicode.com/users/1"
    # Store the result in a variable named 'response'.

    # 4. Print the status code of the response to the terminal (Hint: print(response.status))

    # 5. Use the expect() judge to mathematically verify that the 'response' is ok.
    # (Hint: Playwright has a special assertion for APIs: expect(response).to_be_ok() )