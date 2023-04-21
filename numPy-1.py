#using NumPy to create and manipulate arrays

import numpy as np

# Create a 1-dimensional array
a = np.array([1, 2, 3, 4, 5])
print(a)   # Output: [1 2 3 4 5]

# Create a 2-dimensional array
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)   # Output: [[1 2 3]
           #          [4 5 6]
           #          [7 8 9]]

# Accessing elements of an array
print(a[0])   # Output: 1
print(b[1, 2])   # Output: 6

# Performing operations on arrays
c = np.array([2, 4, 6, 8, 10])
print(a + c)   # Output: [ 3  6  9 12 15]
print(b * c.reshape(3, 1))   # Output: [[ 2  4  6]
                             #          [16 20 24]
                             #          [42 48 54]]
