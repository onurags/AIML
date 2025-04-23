import numpy as np
 class SimpleNeuralNetwork:
    def __init__(self, learning_rate=0.1):
        self.weights = np.random.rand(2, 1) * 0.1
        self.bias = np.random.rand(1) * 0.1
        self.learning_rate = learning_rate
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    def forward(self, inputs):
        self.inputs = inputs
        self.z = np.dot(inputs, self.weights) + self.bias
        self.output = self.sigmoid(self.z)
        return self.output
    def backward(self, error):
        d_output = error * self.sigmoid_derivative(self.output)
        self.weights += self.learning_rate * np.dot(self.inputs.T, 
d_output)
        self.bias += self.learning_rate * np.sum(d_output, axis=0)
    def train(self, inputs, targets, epochs=10000):
        for epoch in range(epochs):
            output = self.forward(inputs)
            error = targets - output
            self.backward(error)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(error))
                print(f"Epoch {epoch}, Loss: {loss}")
 print("Training OR gate")
 X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
 y_or = np.array([[0], [1], [1], [1]])
 or_network = SimpleNeuralNetwork()
 or_network.train(X_or, y_or)
 print("\nTesting OR gate:")
 for i in range(len(X_or)):
    prediction = or_network.forward(X_or[i].reshape(1, 2))
    print(f"Input: {X_or[i]}, Output: {prediction[0][0]}, Expected: 
{y_or[i][0]}")
 print("\nTraining NOR gate")
 y_nor = np.array([[1], [0], [0], [0]])
 nor_network = SimpleNeuralNetwork()
 nor_network.train(X_or, y_nor)
 print("\nTesting NOR gate:")
 for i in range(len(X_or)):
    prediction = nor_network.forward(X_or[i].reshape(1, 2))
    print(f"Input: {X_or[i]}, Output: {prediction[0][0]}, Expected: 
{y_nor[i][0]}")
