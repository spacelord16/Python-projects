import random
import matplotlib.pyplot as plt
import numpy as np
import math


class neuralNetwork :

    def __init__(self,x ,y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1],4)
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np.zeros(self.y.shape)

