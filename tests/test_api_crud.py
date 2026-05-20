from playwright.sync_api import Playwright
from playwright.sync_api import  expect


def test_update_and_delete_user(page):
    updated_data = {"name": "Master SDET", "username": "AutomationPro"}
    put_response = page.request.put("https://jsonplaceholder.typicode.com/users/1", data =updated_data)
    print("Status code: ", put_response.status)
    put_json_response = put_response.json()
    print(put_json_response)



    delete_response = page.request.delete("https://jsonplaceholder.typicode.com/users/1")
    print("Status code: ", delete_response.status)
    delete_json_response = delete_response.json()
    print(delete_json_response)
    expect(delete_response).to_be_ok()








# --- PART 1: UPDATE (PUT) ---
# 1. Create a dictionary named 'updated_data' that changes the user's name to "Master SDET".
# (Hint: updated_data = {"name": "Master SDET", "username": "AutomationPro"} )

# 2. Tell the request engine to perform a .put() action on user #1.
# URL: "https://jsonplaceholder.typicode.com/users/1"
# CRITICAL: Pass your 'updated_data' using the 'data' parameter!
# Store this in a variable named 'put_response'

# 3. Print the put_response.status to the terminal (Should be 200)
# 4. Extract the JSON from put_response and print it so you can see your updated name!


# --- PART 2: DELETE ---
# 5. Tell the request engine to perform a .delete() action on user #1.
# URL: "https://jsonplaceholder.typicode.com/users/1"
# Store this in a variable named 'delete_response'

# 6. Print the delete_response.status to the terminal.
# (Note: Successful deletions usually return a 200 OK or a 204 No Content).

# 7. Use the strict judge to mathematically verify the deletion was successful.
# (Hint: expect(delete_response).to_be_ok() )
