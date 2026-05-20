from core.config import Config

class BaseClient:
    def __init__(self, request_context):
        self.request = request_context
        # SECURE: Dynamically grabbing the URL from the Vault
        self.base_url = Config.API_BASE_URL

    def get_headers(self, token=None):
        # Default headers for every request
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        # If a token is provided (for secure endpoints), inject it
        if token:
            headers["Cookie"] = f"token={token}"

        return headers