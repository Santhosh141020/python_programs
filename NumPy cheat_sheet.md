# NumPy Cheat Sheet

NumPy is the fundamental package for scientific computing with Python.



## Basics 

`axis 0` always refers to row 
`axis 1` always refers to column

| Operator     | Description   |
| :------------- | :------------- |
|`np.array([1,2,3])`|1d array|
|`np.array([(1,2,3),(4,5,6)])`|2d array|
|`np.arange(start,stop,step)`|1d array from start to stop|

### Placeholders 
| Operators | Description |
| :------------- | :------------- |
|`np.linspace(0,2,9)`|Add evenly spaced values btw interval to array of length |
|`np.zeros((1,2))`|Create and array filled with zeros|
|`np.ones((1,2))`|Creates an array filled with ones|
|`np.random.random((5,5))`|Creates random array|
|`np.empty((2,2))`|Creates an empty array|

## 
### Array Properties
|Syntax|Description|
|:-------------|:-------------|
|`array.shape`|Dimensions (Rows,Columns)|
|`len(array)`|Length of Array|
|`array.ndim`|Number of Array Dimensions|
|`array.size`|Number of Array Elements|
|`array.dtype`|Data Type|
|`array.astype(type)`|Converts to Data Type|
|`type(array)`|Type of Array|

### Copying/Sorting 
| Operators | Descriptions     |
| :------------- | :------------- |
|`np.copy(array)`|Creates copy of array|
|`other = array.copy()`|Creates deep copy of array|
|`array.sort()`|Sorts an array|
|`array.sort(axis=0)`|Sorts axis of array|

### Adding or Removing Elements 
|Operator|Description|
|:-----------|:--------|
|`np.append(a,b)`|Append items to array|
|`np.insert(array, 1, 2, axis)`|Insert items into array at axis 0 or 1|
|`np.resize((2,4))`|Resize array to shape(2,4)|
|`np.delete(array,1,axis)`|Deletes items from array|

### Combining Arrays 
|Operator|Description|
|:---------|:-------|
|`np.concatenate((a,b),axis=0)`|Concatenates 2 arrays, adds to end|
|`np.vstack((a,b))`|Stack array row-wise|
|`np.hstack((a,b))`|Stack array column wise|

### Splitting Arrays 
|Operator|Description|
|:---------|:-------|
|`numpy.split()`||
|`np.array_split(array, 3)`|Split an array in sub-arrays of (nearly) identical size|
|`numpy.hsplit(array, 3)`|Split the array horizontally at 3rd index|

### Shaping Arrays 
|Operator|Description|
|:---------|:-------|
|`other = ndarray.flatten()`|Flattens a 2d array to 1d|
|numpy.flip()|Flips order of elements in 1D array|
|np.ndarray[::-1]|Same as above|

|Operator|Description|
|:--------|:--------|
|`other = ndarray.flatten()`|Flattens a 2d array to 1d|
|`array = np.transpose(other)`</br> `array.T` |Transpose array|
|`inverse = np.linalg.inv(matrix)`|Inverse of a given matrix|
### Basic Statistics 
| Operator | Description    |
| :------------- | :------------- |
|`np.mean(array)`|Mean|
|`np.median(array)`|Median|
|`array.corrcoef()`|Correlation Coefficient|
|`np.std(array)`|Standard Deviation|

| Operator | Description    |
| :------------- | :------------- |
|`array.sum()`|Array-wise sum|
|`array.min()`|Array-wise minimum value|
|`array.max(axis=0)`|Maximum value of specified axis|
|`array.cumsum(axis=0)`|Cumulative sum of specified axis|




