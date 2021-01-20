while True:
   value= int(input("Enter the value\n1 Addition\n2 Subtraction\n3 Multiplication\n4 Division\n5 Remainder\n6 exit\n"))
   if value==1:
       a=float(input("Enter a number\n"))
       b=float(input("Enter the another number\n"))
       print("The sum is "+ str(a)+ " + "+ str(b)+ " = "+ str(a+b)+ "\n")
   elif value==2:
        a=float(input("Enter a number\n"))
        b=float(input("Enter the another number\n"))
        print("The difference is "+ str(a)+ " - "+ str(b)+ " = "+ str(a-b)+ "\n")
   elif value==3:
        a=float(input("Enter a number\n"))
        b=float(input("Enter the another number\n"))
        print("The product is "+ str(a)+ " * "+ str(b)+ " = "+ str(a*b)+ "\n")
   elif value==4:
        a=float(input("Enter a number\n"))
        b=float(input("Enter the another number\n"))
        print("The Division is "+ str(a)+ " / "+ str(b)+ " = "+ str(a/b)+ "\n") 
   elif value==5:
        a=float(input("Enter a number\n"))
        b=float(input("Enter the another number\n"))
        print("The Remainder is "+ str(a)+ " % "+ str(b)+ " = "+ str(a%b)+ "\n")
   else :
        break





