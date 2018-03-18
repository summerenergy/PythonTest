import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize

def sigmoid(x):
    return [ (1.0 / ( 1.0 + math.exp( i * -1 ) )) for i in x  ]

def main():
    x = np.arange(-1,1, 0.01)
    w = 10
    b = -50
    z = w * x + b
    print z
    y = sigmoid( z )
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()
