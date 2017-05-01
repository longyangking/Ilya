import numpy as np
import matplotlib.pyplot as plt

def listplot(data):
    x = data[:,0]
    y = data[:,1]
    plt.plot(x,y)
    #plt.draw()
    plt.show(block=True)