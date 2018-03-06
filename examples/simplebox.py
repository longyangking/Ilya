import sys
sys.path.append("..")

import numpy as np 
from ilya.sart import sart2d
from skimage.transform import radon, iradon
import numpy as np
import matplotlib.pyplot as plt

def generate_box():
    theta = range(0,180)
    n = 100
    d = 40
    d1 = 20
    [xv,yv] = np.meshgrid(range(n),range(n))
    box = 1*(xv<=(n/2+d/2))*(xv>=(n/2-d/2))*(yv<=(n/2+d/2))*(yv>=(n/2-d/2)) - 1*(xv<=(n/2+d1/2))*(xv>=(n/2-d1/2))*(yv<=(n/2+d1/2))*(yv>=(n/2-d1/2))
    return box

def generate_projections(fig,theta):
    data = np.rot90(radon(fig,theta=theta))
    projections = np.zeros((data.shape[0],1,data.shape[1]))
    projections[:,0,:] = data
    return projections

if __name__=='__main__':
    fig = generate_box()
    plt.figure()
    plt.title('Original')
    plt.imshow(fig,cmap=plt.cm.Greys_r)
    plt.colorbar()
    plt.savefig('box_original.png')

    theta = range(0,180)
    projections = generate_projections(fig,theta)
    plt.figure()
    plt.title('Projections')
    plt.imshow(projections[:,0,:],cmap=plt.cm.Greys_r)
    plt.colorbar()
    plt.savefig('box_projections.png')

    sartdata = sart2d(angles=theta, projections=projections, verbose=True)
    sartdata.start()
