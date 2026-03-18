class ElectronicDevice():
    def __init__(self,brand):
        self.brand = brand

class Laptop(ElectronicDevice):
    def __init__(self, brand,ram):
        super().__init__(brand)

        self.ram = ram 

E1 = Laptop("HP","16Gb")

print(E1.brand)
print(E1.ram)
        
E2 = Laptop("Lenovo","8Gb")
print(E2.brand)
print(E2.ram)