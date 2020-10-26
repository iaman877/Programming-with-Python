# Access 1-D Arrays
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])   #output 1

# Access 2-D Arrays
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', arr[0, 1])  #output 2nd element on 1st dim:  2

# Negative Indexing 
import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #output Last element from 2nd dim:  10

