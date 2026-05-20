from core.base_client import BaseClient

# BookingClient inherits from BaseClient
class BookingClient(BaseClient):
    def __init__(self, request_context):
        # Pass the request engine up to the BaseClient
        super().__init__(request_context)


    # Make sure this is indented with exactly 4 spaces!
    def create_booking(self, payload):
        # Notice we don't write headers or the full url here anymore!
        response = self.request.post(
            f"{self.base_url}/booking",
            headers=self.get_headers(),
            data=payload
        )
        return response


    # Make sure this is also indented with exactly 4 spaces!
    def delete_booking(self, booking_id, token):
        # We pass the token to our BaseClient, and it builds the secure header for us.
        response = self.request.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers=self.get_headers(token=token)
        )
        return response