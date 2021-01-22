class student:
    def __init__(self):
        self.name = "xxx"
        self.roll = 00
    def inputr(self):
        self.name=input("Enter the name\n")
        self.roll=int(input("Enter the roll no\n"))
    def result(self):
        print(self.name)
        print(self.roll)
class marks(student):
    def __init__(self):
        self.m1=0
        self.m2=0
    def marksi(self):
        self.inputr()
        self.m1=int(input("Enter the marks of first subject\n"))
        self.m2=int(input("Enter the marks of second subject\n"))
    def markso(self):
        self.result()
        print("Average = "+ str((self.m1+self.m2)/2))

m1 = marks()
m1.marksi()
m1.markso()





