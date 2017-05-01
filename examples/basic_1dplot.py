import sys
sys.path.append("..")

import numpy as np 
import ilya

def fun(x):
    return np.sin(x)

if __name__ == '__main__':
    ilya.plot(fun,x=[0,2*np.pi])

    num = 50
    data = np.zeros((num,2))
    data[:,0] = np.linspace(0,5*np.pi,50)
    data[:,1] = np.sin(data[:,0])
    ilya.listplot(data)