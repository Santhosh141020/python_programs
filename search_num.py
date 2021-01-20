array=[]
n=int(input("Enter the number of items\n"))
print("Enter the elements")
for i in range(0,n):
    ele=int(input())
    array.append(ele)
print (array)
ele=int(input("Enter the element to be searched\n"))
for i in range(0,n):
    if array[i]==ele:
        print("Element found at position "+ str(i))
        break
if (array[i]!=ele) :
    print("Element not found\n")
    
