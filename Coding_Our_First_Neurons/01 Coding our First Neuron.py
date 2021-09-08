import random
from random import uniform
import sys
sys.stdout = open("01 Coding our First Neuron.txt", "w")

# Let’s say we have a single neuron, and there are three inputs to this neuron.
inputs = [1, 2, 3]
print("Let’s say we have a single neuron, and there are three inputs to this neuron :", inputs, "\n")

# Each input also needs a weight associated with it.
weights = [0.2, 0.8, -0.5]
print("Each input also needs a weight associated with it :", weights, "\n")

# At the moment, we’re modeling a single neuron with three inputs. Since we’re modeling a single neuron, we only have one bias,
# as there’s just one bias value per neuron.
bias = 2
print("Since we’re modeling a single neuron, we only have one bias :", bias, "\n")

# This neuron sums each input multiplied by that input’s weight, then adds the bias.
output = (inputs[0] * weights[0] +
          inputs[1] * weights[1] +
          inputs[2] * weights[2] + bias)
print("Neuron output :", output, "\n")

print("What if we have N number of inputs . . .", "\n")


def neuron(num_inputs):
    neuron_inputs = random.sample(range(0, 100), num_inputs)
    neuron_weights = [uniform(-1.0, 1.0) for _ in range(0, num_inputs)]
    bias = uniform(-1.0, 1.0)
    print("N =", num_inputs)
    print("Inputs =", neuron_inputs)
    print("Weights =", neuron_weights)
    print("Bias =", bias)
    # return (neuron_inputs, neuron_weights, bias)
    # return {"Neuron inputs" : neuron_inputs, "Neuron weights" : neuron_weights, "Neuron bias" : bias}
    return [neuron_inputs, neuron_weights, bias]


new_inputs = neuron(num_inputs = 5)
# TASK : Write a function to calculate the output of a Neuron for each data structure type
# print(new_inputs)

"""
def neuron_output(inputs, weights, bias):
    for i in range(0, len(inputs)):
        i = 0
        for j in range(0, len(weights)):
            j = 0
            if i == j:
                ith_cal = inputs[i]*weights[j]
            else:
                print("This Neuron is not a part of Fully connected Neural Network")
            j += 1
            i += 1
    i_plus_1_th_cal = ith_cal + inputs[i]*weights[j]
    output = i_plus_1_th_cal + bias
    return output
"""

def neuron_output(inputs, weights, bias):
    i_plus_1_th_cal = [x*w for x,w in zip(inputs, weights)]
    output = sum(i_plus_1_th_cal, bias)
    return output


neuron = neuron_output(inputs, weights, bias)
print(neuron)

sys.stdout.close()
