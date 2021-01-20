# TUPLES IN PYTHON

#### They are immutable means they can't be edited 

###  Various methods to create a tuple

1. declaring elements inside the common brackets

   ```python
   tu=(1,2,3,4,5)
   ```

2. Just using assignment operation

   ```python
   tu1=1,2,3,4,5
   #type(tu1)
   #<class 'tuple'>
   ```

    

### Accessing elements in Tuple

it is similar to the list , we used just use index value to access it

even slicing can also be used

```python
print(tu1[0])
print(tu1[1:]) #to print alle the elements from 2 to end
print(tu1[:-1]) #to print them in reverse order
print(tu1[::2]) #to print alternate numbers	
```

### Function or attributes of Tuple

1. index()

   it returns the index of certain element in tuple

   ```python
   tu1.index(2)
   #it returns the index as 1
   ```

2. count()

   it returns the number of times an element is repeated

   ```python
   tu1.count(3)
   #it returns as 1 
   ```

### Delete an tuple

we can't delete tuple elements individually but we can delete tuple entirely using a keyword **del**

```python
del tu1
```

 
