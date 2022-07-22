class Animal:

    def __int__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("I am barking")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog("Max","Golden retriever")
dog.speak()
print(dog.name)
print(dog.breed)