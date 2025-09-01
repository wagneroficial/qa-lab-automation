# utils.py
from faker import Faker

fake = Faker(locale="pt_BR") 

def generate_fake_user():
    return {
        "name": fake.name(),
        "company": "Konneqt",
        "phone": fake.phone_number(),
        "email": fake.email()
    }
