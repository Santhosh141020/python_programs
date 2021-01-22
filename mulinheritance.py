class A :
    def __init__(self):
        self.a=0

    def take(self):
        self.a=int(input("Enter a number\n"))

class B :
    def __init__(self):
        self.b=0

    def inp(self):
        self.b=int(input("Enter the another number\n"))

class C(A, B) :
    def out(self):
        self.take()
        self.inp()
        print("Multiplication table from "+ str(self.a)+ " to "+ str(self.b))
        for i in range(self.a,self.b+1):
            for j in range(1,11):
                print(str(i)+ " * "+ str(j)+ " = "+ str(j*i))
            print("\n")
obj = C()
obj.out()


