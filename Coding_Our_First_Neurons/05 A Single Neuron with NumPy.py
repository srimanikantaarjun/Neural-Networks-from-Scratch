import numpy as np
import sys
sys.stdout = open("05 A Single Neuron with NumPy.txt", "w")

inputs = [1.0, 2.0, 3.0, 2.5]
print("Inputs :", inputs, "\n")
weights = [0.2, 0.8, -0.5, 1.0]
print("Weights :", weights, "\n")
bias = 2.0
print("Bias :", bias, "\n")

outputs = np.dot(weights, inputs) + bias
print("Dot product output :", outputs, "\n")

sys.stdout.close()
