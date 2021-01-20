class student:
    def __init__(self):
        pass

    def input(self):
        self.name=input("Enter the student name\n")
        self.usn=input("Enter the university seat number\n")
        self.gpa=input("Enter the CGPA\n")
    def output(self):
        print("The students details are")
        print(self.name)
        print(self.usn)
        print(self.gpa)


s1 =student()
s1.input()
s1.output()

