import pytest
import string
import random
from selenium import webdriver
from faker import Faker


@pytest.fixture()
def email():
    faker = Faker()
    mail = faker.email()
    return mail


@pytest.fixture()
def password():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    pass_word = []
    for pass_word_len in range(6):
        pass_word.append(random.choice(characters))
    random.shuffle(pass_word)
    return "".join(pass_word)


@pytest.fixture(scope='function')
def driver(request):
    driver = webdriver.Chrome()
    driver.get(request.param)
    yield driver
    driver.quit()
