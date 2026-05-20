class AuthClient:
    def __init__(self, request_context):
        # We pass Playwright's request engine directly into the client
        self.request = request_context
        # Hardcoding for today; we will pull this from .env shortly!
        self.base_url = "https://restful-booker.herokuapp.com"

    def get_token(self, username="admin", password="password123"):
        # 1. Tell the request engine to POST to the /auth endpoint
        response = self.request.post(
            f"{self.base_url}/auth",
            data={"username": username, "password": password}
        )

        # 2. Extract the JSON response
        json_data = response.json()

        # 3. Return ONLY the string value of the "token" key
        return json_data["token"]