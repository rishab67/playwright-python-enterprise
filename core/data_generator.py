from faker import Faker
import random

class DataGenerator:
    def __init__(self):
        # Wake up the Faker library once for the whole class
        self.fake = Faker()

    # Assembly Line 1: For UI Tests (Users)
    def generate_random_user(self):
        return{
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "email": self.fake.email(),
            "phone": self.fake.phone_number(),
            "password": self.fake.password(length=12),
        }





    # Assembly 2: For API Tests (Hotel Bookings)
    def generate_booking_payload(self):
        # Every time this is called, it invents a completely new, randomized dictionary
        return {
            "firstname": self.fake.first_name(),
            "lastname": self.fake.last_name(),
            "totalprice": random.randint(100, 5000),
            "depositpaid": random.choice([True, False]),
            "bookingdates": {
                "checkin": "2026-06-01",
                "checkout": "2026-06-10"
            },
            "additionalneeds": random.choice(["Breakfast", "Late Checkout", "Extra Pillows"])
        }