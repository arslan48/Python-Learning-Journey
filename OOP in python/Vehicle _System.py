class Vehicle():
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed,doors):
        super().__init__(brand, speed)

        self.doors = doors

c1 = Car("Toyota", 120, 4)

print(c1.doors)
print(c1.brand)
print(c1.speed)
