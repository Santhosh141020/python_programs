class A :
    def __init__(self):
        self.a=1
    def take(self):
        self.a=int(input("Enter the length of pattern\n"))

class B(A):
    def __init__(self):
       # super().__init__()
        self.b="*"

    def pattern(self):
        self.take()
        self.b=input("Enter a character\n")
        print()
        for i in range (1,self.a+1):
            for j in range(0,i):
                print(self.b,end="")
            print("") 
obj = B()
obj.pattern()

