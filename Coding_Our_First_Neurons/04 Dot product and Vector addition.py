import sys
sys.stdout = open("04 Dot product and Vector addition.txt", "w")

a = [1, 2, 3]
b = [2, 3, 4]

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print("Dot product of two vectors (similar to high school linear algebra)", dot_product)

sys.stdout.close()
