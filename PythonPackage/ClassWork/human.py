# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int
    gender: str


human = Human("Ololade", 24, "F")
print(human)
