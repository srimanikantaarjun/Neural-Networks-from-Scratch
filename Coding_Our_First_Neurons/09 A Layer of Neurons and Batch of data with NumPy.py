import numpy as np
import sys
sys.stdout = open("09 A Layer of Neurons and Batch of data with NumPy.txt", "w")

inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],        # (3, 4)
          [-1.5, 2.7, 3.3, -0.8]]
print("Inputs :", inputs, "\n")

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],        # (3, 4) * (3, 4) the no. of cols of the left matrix should be equal to no. of rows in the right matrix
           [-0.26, -0.27, 0.17, 0.87]]
print("Weights :", weights, "\n")
print("Weights after transposed :\n", np.array(weights).T, "\n")

biases = [2.0, 3.0, 0.5]
print("Biases ", biases, "\n")

layer_outputs = np.dot(inputs, np.array(weights).T) + biases
print("Layer Outputs :\n", layer_outputs)

sys.stdout.close()
