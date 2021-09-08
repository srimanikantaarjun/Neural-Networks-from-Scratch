import numpy as np
import sys
sys.stdout = open("06 A Layer of Neurons with NumPy.txt", "w")

inputs = [1.0, 2.0, 3.0, 2.5]
print("Inputs :", inputs, "\n")

weights = [[0.2, 0.8, -0.5, 1],
             [0.5, -0.91, 0.26, -0.5],
             [-0.26, -0.27, 0.17, 0.87]]
print("Weights :", weights, "\n")

biases = [2.0, 3.0, 0.5]
print("Bias :", biases, "\n")

layer_outputs = np.dot(weights, inputs) + biases
print("Layer outputs by dot product using numpy :", layer_outputs, "\n")

print("To explain the order of parameters we are passing into np.dot(), we should think of it as whatever comes first will decide the output shape. \n"
      "In our case, we are passing a list of neuron weights first and then the inputs, as our goal is to get a list of neuron outputs. \n"
      "As we mentioned, a dot product of a matrix and a vector results in a list of dot products. \n"
      "The np.dot() method treats the matrix as a list of vectors and performs a dot product of each of those vectors with the other vector. \n"
      "In this example, we used that property to pass a matrix, which was a list of neuron weight vectors and a vector of inputs and get a list of dot products — neuron outputs.\n")

sys.stdout.close()
