from playwright.sync_api import expect


def test_create_user(page):
# 1. Create a standard Python dictionary holding your new user's data.
    new_user = {"name": "Senior QA Engineer", "username": "AutomationPro"}
    response = page.request.post("https://jsonplaceholder.typicode.com/users", data=new_user)
    print("Status code:", response.status)
    expect(response).to_be_ok()
    json_data = response.json()
    print(json_data)



# Store it in a variable named 'new_user'.
# (Hint: new_user = {"name": "Senior QA Engineer", "username": "AutomationPro"} )

# 2. Tell the page's request engine to perform a .post() action to exactly "https://jsonplaceholder.typicode.com/users"
# CRITICAL: You must pass your 'new_user' dictionary into the API call using the 'data' parameter!
# (Hint: response = page.request.post("https://jsonplaceholder.typicode.com/users", data=new_user) )

# 3. Print the status code to the terminal.
# (Note: For a successful POST creation, servers typically respond with a 201 Status Code instead of 200).

# 4. Use Playwright's Strict Judge to verify the response is OK (expect.to_be_ok()).

# 5. Extract the JSON response into a variable named 'json_data', then print it to the terminal so you can physically see the database echoing your newly created user!