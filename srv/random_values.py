import random
import string


def random_int(i_min, i_max, disable: tuple = ()):
    index = random.randint(i_min, i_max)
    if index in disable:
        return random_int(i_min, i_max, disable)
    return index


def random_string(length=5):
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])


def random_phone(length=11):
    return "".join([random.choice(string.digits) for _ in range(length)])


def random_email():
    return random_string(10) + '@' + random_string() + '.' + random.choice(['com', 'ru', 'ua', 'org'])
