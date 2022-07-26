# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

from dataclasses import dataclass, field


@dataclass(order=True)
class Human:
    name: str
    age: int = field(default=0)
    gender: str = field(default='F')
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)


human = Human("Ololade", 24, "F")
alien = Human("Boyo", 45, "M")
print(human < alien)
