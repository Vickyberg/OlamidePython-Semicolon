class Person:
    def __init__(self, name: str, age: 17) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        print("Name will now be deleted")
        del self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self._age = new_age


person1 = Person("Abigail",33)
person2 = Person("Dorcas",56)

print(person1.name)
person1.name = "Ola"

del person1.name
print(person1.name)
print(dir(person1))
