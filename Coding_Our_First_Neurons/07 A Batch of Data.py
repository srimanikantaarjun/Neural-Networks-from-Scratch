import sys
sys.stdout = open("07 A Batch of Data.txt", "w")

inputs = [1, 2, 3, 2.5]
print("Inputs :", inputs, "\n")

print("Often, neural networks expect to take in many samples at a time for two reasons. One reason is that it’s faster to train in batches in parallel processing, \n"
      "and the other reason is that batches help with generalization during training. If you fit (perform a step of a training process) on one sample at a time, \n"
      "you’re highly likely to keep fitting to that individual sample, rather than slowly producing general tweaks to weights and biases that fit the entire dataset. \n"
      "Fitting or training in batches gives you a higher chance of making more meaningful changes to weights and biases.\n")

feature_set = [[1, 2, 3, 2.5], [2, 5, -1, 2], [-1.5, 2.7, 3.3, -0.8]]
print("Feature set :", feature_set, "\n")
print(f"Samples / Feature set instances / Observations : {feature_set[0]}, {feature_set[1]} and {feature_set[2]}", "\n")

sys.stdout.close()
