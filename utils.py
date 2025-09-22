from faker import Faker
import re

fake = Faker("pt_BR")

def clean_name(name):
    """Remove títulos e caracteres especiais do nome"""
    # Remove títulos comuns
    titles = ['Sr.', 'Sra.', 'Dr.', 'Dra.', 'Prof.', 'Profa.']
    
    for title in titles:
        name = name.replace(title, '').strip()
    
    # Remove pontos extras e espaços duplos
    name = re.sub(r'\.+', '', name)  # Remove pontos
    name = re.sub(r'\s+', ' ', name)  # Remove espaços duplos
    
    return name.strip()

def get_user_data(scenario):
    # Gera nome limpo sem títulos
    raw_name = fake.name()
    clean_full_name = clean_name(raw_name)
    
    base_data = {
        "name": clean_full_name,
        "phone": fake.phone_number(),
    }
    
    scenarios = {
        "valid": {"company": "Konneqt", "email": fake.email()},
        "invalid_company": {"company": "EmpresaInexistente", "email": fake.email()},
        "user_exists": {"company": "Konneqt", "email": "admin@konneqt.io"}
    }
    
    return {**base_data, **scenarios[scenario]}