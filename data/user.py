import dataclasses
from enum import Enum
from datetime import date


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Hobbies(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone: str
    birth_date: date
    subject: str
    hobby: Hobbies
    picture: str
    address: str
    state: str
    city: str


user = User(
    'Alexey',
    'Kokorev',
    'test@gmail.ru',
    Gender.male.value,
    '1234567890',
    date(1991, 5, 15),
    'Maths',
    Hobbies.sports.value,
    'bat.png',
    'Bali, Ubud, 1',
    'NCR',
    'Delhi'
)
