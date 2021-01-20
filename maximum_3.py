def max(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


num1=int(input("Enter a number\n"))
num2=int(input("Enter a second  number\n"))
num3=int(input("Enter a third  number\n"))
print("The maximum number is "+str(max(num1,num2,num3)))




