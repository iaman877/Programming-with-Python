# NumPy is used to work with arrays. The array object in NumPy is called ndarray. We can create a NumPy ndarray object by using the array() function.
# 1 Introction to numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
"""
output:
[1 2 3 4 5]
<class 'numpy.ndarray'>
"""
_________________________________________________

# Use a tuple to create a NumPy array:
import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)  #[1 2 3 4 5]
__________________________________________________

# Dimensions in Arrays :
"""
A dimension in arrays is one level of array depth (nested arrays).
nested array: are arrays that have arrays as their elements.
> 0-D Arrays :
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
"""
import numpy as np
arr = np.array(42)
print(arr)     # 42

# 1-D Arrays :An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)  #[1 2 3 4 5]

#2-D Arrays
"""
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.
NumPy has a whole sub module dedicated towards matrix operations called numpy.mat
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
# output [[1 2 3][4 5 6]]

# 3-D arrays
"""
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
These are often used to represent a 3rd order tensor.
"""
import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr) 
"""
[[[1 2 3]
  [4 5 6]]

 [[1 2 3]
  [4 5 6]]]
 """

# Check Number of Dimensions : NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
import numpy as np
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
"""
Output:
0
1
2
3
"""
# Higher Dimensional Arrays
"""
An array can have any number of dimensions.
When the array is created, you can define the number of dimensions by using the ndmin argument.
Example
Create an array with 5 dimensions and verify that it has 5 dimensions:
"""
import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

"""
[[[[[1 2 3 4]]]]]
number of dimensions : 5
"""
