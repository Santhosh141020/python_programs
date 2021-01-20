n=int(input("Enter the number of  elements\n"))
s=[]
print("Enter the elements")
for i in range(0,n):
    ele=int(input())
    s.append(ele)
print("The ascending order is \n")
s.sort()
print(s)
print("The desending order is \n")
s.reverse()
print(s)
