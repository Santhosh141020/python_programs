p=int(input("Enter a number\n"))
mul=0
for i in range(1,p+1):
    if p%i==0:
        mul+=1
if mul==2:
    print("It is prime number\n")
else :
    print("It is composite number\n")


