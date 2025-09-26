from faker import Faker

class TestDataGenerator:
    @classmethod
    def generate_valid_user(cls):
        fake = Faker('pt_BR')
        
        return {
            'name': fake.name(),
            'email': fake.email(),
            'password': 'MinhaSenh@123'
        }
