import sys
sys.stdout = open("02 A Layer of Neurons.txt", "w")

inputs = [1, 2, 3, 2.5]
print("Inputs :", inputs, "\n")

weights1 = [0.20, 0.80, -0.5, 10]
weights2 = [0.50, -0.91, 0.26, -0.50]
weights3 = [-0.26, -0.27, 0.17, 0.87]
print(f"We have 3 neurons so we have 3 sets/lists of weights and for {len(inputs)} inputs :", "\n")
print("Weights for 1st neuron :", weights1, "\n")
print("Weights for 2nd neuron :", weights2, "\n")
print("Weights for 3rd neuron :", weights3, "\n")

bias1 = 2
bias2 = 3
bias3 = 0.5
print("Similarly, 3 bias, 1 for each neuron :", "\n")
print("Bias for 1st neuron :", bias1, "\n")
print("Bias for 2nd neuron :", bias2, "\n")
print("Bias for 3rd neuron :", bias3, "\n")

output = ((inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1),
          (inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2),
          (inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3))
print("Layer output :", output, "\n")

print("In the above code, we have three sets of weights and three biases, which define three neurons. Each neuron is “connected” to the same inputs. \n"
      "The difference is in the separate weights and bias that each neuron applies to the input. This is called a fully connected neural \n"
      "network — every neuron in the current layer has connections to every neuron from the previous layer. This is a very common type of neural network, \n"
      "but it should be noted that there is no requirement to fully connect everything like this.\n")

# Let's write a similar function to our previous exercise to calculate output of a layer of neurons
def layer_output(inputs, weights, biases):
    layer_output = []
    for neuron_weights, neuron_bias in zip(weights, biases):
        neuron_output = 0
        for neuron_input, weight in zip(inputs, neuron_weights):
            neuron_output += neuron_input*weight
        neuron_output += neuron_bias
        layer_output.append(neuron_output)
    return layer_output

Layer_Output = layer_output(inputs, [weights1, weights2, weights3], [bias1, bias2, bias3])
print("Layer Output using a function:", Layer_Output, "\n")

sys.stdout.close()
