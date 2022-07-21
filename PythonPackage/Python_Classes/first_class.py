class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        print("You're calling me")
        return self._name

    @name.setter
    def name(self, name):
        print("Setter")
        if "f" in name:
            print("Fuck Off")
            return
        self._name = name


person1 = Person("Abigail")
person1.name = "Omotee f"

print(person1.name)
