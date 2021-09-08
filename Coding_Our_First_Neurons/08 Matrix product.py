import numpy as np
import sys
sys.stdout = open("08 Matrix product.txt", "w")

print("The matrix product is an operation in which we have 2 matrices, and we are performing dot products of all combinations \n"
      "of rows from the first matrix and the columns of the 2nd matrix, resulting in a matrix of those atomic dot products.\n")

a = [1, 2, 3]
row_vector = np.array([a])
print("Row vector :", row_vector, "\n")
print("We can create a row vector using np.expand_dims() as well adding an extra dimension along the 1st dimension (axis = 0).\n")
row_vector1 = np.expand_dims(np.array(a), axis = 0)
print("Using np.expand_dims() :", row_vector1, "\n")

b = [2, 3, 4]
col_vector = np.array([b]).T
print("We can create a column vector by applying transposition method to a list/1D - array/1D - vector.")
print("Column vector :\n", col_vector, "\n")
print("Dot product (technically matrix product) of a row vector and column vector :", np.dot(a, b))

print("NumPy does not have a dedicated method for performing matrix product — the dot product and matrix product are both implemented in a single method: np.dot()")

sys.stdout.close()
