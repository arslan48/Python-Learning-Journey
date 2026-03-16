class Car():
    def __init__(self,name):
        self.name = name
    def models(self):
        print(self.name)
c1 = Car("Civic")
c2 = Car("Corolla")

c1.models()
c2.models()
