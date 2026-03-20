class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"Hellow {self.name} your avg marks are {sum/3}.")
        
s1 = Student("Alice",[45,57,57])
s1.get_avg()