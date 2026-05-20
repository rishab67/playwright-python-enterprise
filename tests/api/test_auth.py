# 1. Import your brand new AuthClient wrapper
from api_clients.auth_client import AuthClient


def test_generate_auth_token(page):
    # 2. Initialize the client, handing it Playwright's request engine
    auth_client = AuthClient(page.request)

    # 3. Call your custom method to generate the token
    token = auth_client.get_token()

    # 4. Print the token to the terminal so we can physically see it
    print(f"\nSECURE TOKEN GENERATED: {token}")

    # 5. Standard Python assertions to mathematically prove the token exists
    assert token is not None
    assert type(token) == str
    assert len(token) > 0