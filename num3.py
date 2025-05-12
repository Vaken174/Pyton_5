import random
import json
import string


def generate_random_fullname():
    possible_firstnames = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Emma"]
    possible_lastnames = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller"]
    return f"{random.choice(possible_firstnames)} {random.choice(possible_lastnames)}"


def generate_user_email(fullname):
    firstname, lastname = fullname.lower().split()
    email_domains = ["gmail.com", "yahoo.com", "example.com", "outlook.com", "hotmail.com"]
    return f"{firstname}.{lastname}@{random.choice(email_domains)}"


def create_random_password(password_length=12):
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(allowed_chars) for _ in range(password_length))


def create_user_profile():
    user_fullname = generate_random_fullname()
    user_age = random.randint(18, 80)
    user_email = generate_user_email(user_fullname)
    user_password = create_random_password()

    return {
        "fullname": user_fullname,
        "age": user_age,
        "email": user_email,
        "password": user_password
    }


def export_to_json(user_profile, output_file="user_data.json"):
    with open(output_file, 'w') as json_file:
        json.dump(user_profile, json_file, indent=4)


def import_from_json(input_file="user_data.json"):
    with open(input_file, 'r') as json_file:
        return json.load(json_file)


user_profile = create_user_profile()# Генерируем профиль пользователя

export_to_json(user_profile)# Экспорт

imported_profile = import_from_json()
print(json.dumps(imported_profile, indent=4))