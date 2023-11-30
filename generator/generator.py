import os
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
        mobile=faker_en.msisdn()
    )


# def generating_file():
#     path = f"C:\\Users\\IT Centre 2 in 1\\portfolio_ui_automation\\test_file{random.randint(0, 999)}.txt"
#     file = open(path, 'w+')
#     file.write(f'Random text{random.randint(0, 999)}')
#     file_name = file.name
#     file.close()
#     return file_name, path

def generating_file():
    current_directory = os.getcwd()
    file_name = f"test_file{random.randint(0, 999)}.txt"
    path = os.path.join(current_directory, file_name)
    with open(path, 'w+') as file:
        file.write(f'Random text{random.randint(0, 999)}')
    return file_name, path


def generating_subjects():
    subjects = {
        1: "Hindi",
        2: "English",
        3: "Maths",
        4: "Physics",
        5: "Chemistry",
        6: "Biology",
        7: "Computer Science",
        8: "Commerce",
        9: "Accounting",
        10: "Economics",
        11: "Arts",
        12: "Social Studies",
        13: "History",
        14: "Civics"
    }
    count = 5
    random_list_of_subjects = []
    while count != 0:
        random_subject = subjects[random.randint(1, 14)]
        if random_subject not in random_list_of_subjects:
            random_list_of_subjects.append(random_subject)
            count -= 1
    return random_list_of_subjects


