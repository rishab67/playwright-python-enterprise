from core.data_generator import DataGenerator


def test_enterprise_data_factory():
    # 1. Wake up the Factory
    factory = DataGenerator()

    # 2. Order one of each product
    new_ui_user = factory.generate_random_user()
    new_api_booking = factory.generate_booking_payload()



    # 3. Print them so we can audit the output
    print(f"\n[UI PAYLOAD] Random User: {new_ui_user}")
    print(f"\n[API PAYLOAD] Random Booking: {new_api_booking}")


    # 4. Mathematically prove they generated successfully
    assert "email" in new_ui_user
    assert "totalprice" in new_api_booking