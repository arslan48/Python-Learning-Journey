class Phone():
    def __init__(self,brand,model):
        
        self.brand = brand
        self.model = model

    def call(self):
        print(f"Calling from {self.brand} {self.model}")
class Smartphone(Phone):
    def __init__(self, brand, model,OS):
        super().__init__(brand, model)

        self.OS = OS
    def brwose(self):
        print(f"Browsing on {self.OS}")

p1 = Smartphone("Samsung","A52s","Android")
p1.call()
p1.brwose()   