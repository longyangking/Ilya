import numpy as np 
import scipy as sp
import scipy.ndimage as spn
import pdb
import time

import matplotlib.pyplot as plt

class sart2d:
    def __init__(self, angles, projections, pslice=None, iterations=50, relax=1.0, parallelize=False, verbose=False):
        self.projections = projections
        self.angles = angles
        self.pslice = pslice
        self.iterations = iterations

        self.n_proj, self.nx, self.ny = projections.shape

        self.reco = sp.zeros((self.ny, self.ny))

        self.relax = relax
        self.parallelize = parallelize
        self.verbose = verbose

    def start(self,filename='sart2d'):
        self.wij_sum = sp.zeros((self.ny, self.ny))

        if self.pslice is None:
            slice_range = range(self.nx)
        else:
            slice_range = [self.pslice]

        for self.pslice in slice_range:
            self.reco = sp.zeros((self.ny, self.ny))
			
            sinogram = self.projections[:,self.pslice,:]

            for it in range(self.iterations):
                self.upd = sp.zeros_like(self.reco)
                for i in range(self.n_proj):
                    then = time.time()
				
                    reco = self.reco.copy()
                    angle = self.angles[i]
                    p = sinogram[i,:] 
                    upd = sp.zeros_like(reco)
                    wij_sum = sp.zeros_like(reco)
                    chunk = range(self.ny)
                    for j in chunk:
                        ray = sp.zeros_like(reco)
                        ray[:,j]=1
                        wij = spn.rotate(ray, angle, reshape=False)
                        upd += ((p[j]-sp.sum(wij*reco))/sp.sum(wij**2.0))*wij
                        if it==0:
                            wij_sum+=wij
                    if it==0:
                        self.wij_sum += wij_sum
                    self.upd+=upd
							
                    if (i%10==0) and self.verbose:
                        print('Iter: {:d}, Proj: {:d}, Duration: {:3.2f} sec'.format(it, i, time.time()-then))

                if (it==0) and self.verbose:
                    self.reco+=self.upd/(self.wij_sum+0.1)
                else:
                    self.reco+=self.relax*self.upd/(self.wij_sum+0.1)

                if self.verbose:
                    print("Save result...")
                self.savefigure(it=it,filename=filename)

    def savefigure(self, it, filename):
        plt.imshow(self.reco, cmap=plt.cm.Greys_r)
        plt.title('Iteration {it}'.format(it=it))
        plt.savefig('{filename}_{it}.png'.format(filename=filename,it=it))







	