class shape():
    def draw(self):
        print("Drawing a shape")

class Triangle(shape):
    def draw(self):
        print("Drawing a Triangle")
        
class Circle(shape):
    def draw(self):
        print("Drawing a Circle")

s1 = Triangle()
s2 = Circle()

s1.draw()
s2.draw()