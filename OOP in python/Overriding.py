class ElectronicDevice:
    def power_on(self):
        print("Device is starting")
class Laptop(ElectronicDevice):
    def power_on(self):
        print("Laptop is booting")

b1 = Laptop()
b1.power_on()
