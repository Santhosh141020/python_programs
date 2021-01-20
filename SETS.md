# SETS

it does not contain duplicate items 

### To create a new set

1. Using a function set()

   ```python
   s1=set([2,3,4,5])
   # set function takes a maximum of one argument so they must be specified as list but it treates them as seperate element
   ```

2. Using flower braces

   ```python
   s2={2,6,4,7,8}
   ```

   flower braces should not be used to create an empty set because it creates an empty dictionary instead

### To add an element to the set

1. to add an single element use **add()** function

   ```python
   s1.add(6)
   ```

2. To append multiply elements we can use **update()** 

   update function takes only list and set as it's arguments. But there is no limit to  the number of arguements 

   ```python
   s3=set()
   s3.update([9,8,7,6],s2)
   ```

### Function in SETS

1. Intersection

   ```python
   s4=s1.intersection(s2)
   s5=s1.intersection(s2,s3) # if we want to perform intersectioon of more than 2 sets 
   ```

2. Union

   it performs union operation. function operation is simliar to intersection function

3. Difference

   ```python
   s4=s1.difference of(s2) #s1-s2
   s4=s1.difference of(s2,s3) #s1-s2-s3
   ```

4. symmetric_difference

   ```python
   s4=s1.symmetric_difference of(s2) #it returns a elements which are unique in bot a and b i.e (a intersection b)'
   ```

   



### To remove an element from the set

1. remove()

   Element to be removed must be given as argument not the index value.

   If the element is not present in set **it gives an error**

   ```python
   s3.remove(6)
   s3.remove(10) #it gives an error
   ```

    

2. discard()

   Element to be removed must be given as argument not the index value.

   If the element is not present in set, **it does not how any error**













