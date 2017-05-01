import numpy as np
import matplotlib.pyplot as plt
#import ..ext as ext

def plot(fun,x,plotpoints=30):
    [LB,UB] = x
    x = np.linspace(LB,UB,plotpoints)
    y = fun(x)
    plt.plot(x,y)
    #plt.draw()
    plt.show(block=True)