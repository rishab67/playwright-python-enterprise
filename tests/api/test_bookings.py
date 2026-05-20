from core.data_generator import DataGenerator


# Notice we pass in the 'booking_manager' fixture here!
def test_booking_lifecycle_with_fixture(booking_manager):
    # 1. Unpack our tools from the global manager (conftest.py)
    booking_client, trash_list = booking_manager
    data_factory = DataGenerator()


    # 2. Generate and Send Data
    new_booking = data_factory.generate_booking_payload()
    create_response = booking_client.create_booking(new_booking)


    # 3. Add the ID to the trash list IMMEDIATELY so the manager knows what to delete!
    booking_id = create_response.json()['bookingid']
    trash_list.append(booking_id)


    # 4. Mathematically prove the DB saved our DYNAMIC data
    assert create_response.status == 200
    assert create_response.json()["booking"]["firstname"] == new_booking["firstname"]
    print(f"\n[✅] Created Booking ID: {booking_id}")

    # LOOK! No teardown code. No tokens.
    # When this test ends, the 'yield' in conftest.py automatically wakes up and deletes it.