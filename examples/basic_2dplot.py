import sys
sys.path.append("..")

import numpy as np 
import ilya

def fun(x,y):
    return np.sin(np.square(x) + np.square(y))

if __name__ == '__main__':
    ilya.densityplot(fun,x=[-np.pi,np.pi],y=[-np.pi,np.pi])

    num = 100
    data = np.zeros((num,3))
    x = np.linspace(-np.pi,np.pi,num)
    data[:,0] = x[:]
    data[:,1] = x[:]
    data[:,2] = np.sin(x)*np.cos(x)
    ilya.listdensityplot(data)
