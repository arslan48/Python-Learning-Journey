class Moblile():
    def __init__(Self,brand,price):
        Self.brand = brand
        Self.price = price
    def show_details(self):
        print(f"brand: {self.brand}\n price of moblie is: {self.price}")

m1 =Moblile("samsung", 45000)
m2 =Moblile("Redmi", 60000)

m1.show_details()  
m2.show_details()  