import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')
Faker.seed()


def generating_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_en.job()[:24],
        email=faker_en.email(),
        current_address=faker_en.address(),
        permanent_address=faker_en.address(),
        # mobile=faker_en.msisdn()
    )


def generating_file():
    path = f"C:\\Users\\IT Centre 2 in 1\\portfolio_ui_automation\\test_file{random.randint(0, 999)}.txt"
    file = open(path, 'w+')
    file.write(f'Random text{random.randint(0, 999)}')
    file.close()
    return file.name, path
