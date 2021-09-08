import sys
sys.stdout = open("03 Tensors, Arrays and Vectors.txt", "w")

l = [1, 2, 3, 4]
print("List/Vector/1-D Array/Linear array :", l, "\n")

lol = [[1, 2, 3, 4],
       [5, 6, 7, 8]]
print("List of lists/2-D Array/Matrix/2-D vector :", lol, "\n")

lolol = [[[1, 2, 3, 4],
          [5, 6, 7, 8]],
         [[9, 10, 11, 12],
          [13, 14, 15, 16]],
         [[17, 18, 19, 20],
          [21, 22, 23, 24]],
         [[25, 26, 27, 28],
          [29, 30, 31, 32]]]
print("List of lists of lists/4-D Array/Tensor :\n", lolol, "\n")
print("The above list contains 4 lists inside it each with 2 lists inside them each with 4 elements in them so \n"
      "the shape/dimension of the above list is (4, 2, 4)\n")

lol2 = [[1, 2, 3, 4],
        [5, 6]]
print("Another List of lists :", lol2)
print("The above list of lists cannot be an array because it is not homologous. \nA list of lists is homologous "
      "if each list along a dimension is identically long, and this must be true for each dimension.")

sys.stdout.close()
