class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self, name, age,breed):
        super().__init__(name, age)

        self.breed = breed
    def show_info(self):
        print(f"Name: {self.name} Age: {self.age} Breed: {self.breed}")

d1 = Dog("Buddy" ,3, "German Shepherd")
d1.show_info()