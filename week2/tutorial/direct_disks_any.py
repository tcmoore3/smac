import matplotlib as mpl
mpl.use('Agg')
import random, math, pylab
import itertools
import numpy as np
import ipdb

def dist(x, y):
    d_x = abs(x[0] - y[0]) % 1.0
    d_x = min(d_x, 1.0 - d_x)
    d_y = abs(x[1] - y[1]) % 1.0
    d_y = min(d_y, 1.0 - d_y)
    return  math.sqrt(d_x**2 + d_y**2)
    
def run(N, n_confs=10e5): 
    pairs = [(i, j) for i, j in itertools.combinations(range(N), 2)]
    eta_maxs = np.empty(n_confs)
    for conf in xrange(n_confs):

        # put disks at random positions
        L = [(random.random(), random.random()) for k in range(N)]

        # the largest possible radius based on the nearest neighbors
        sigma_max = min(dist(L[i], L[j]) for i, j in pairs) / 2.0

        # eta_max is the maximum density based on the closest neighbors
        # divide by the area of the box
        eta_maxs[conf] = N * math.pi * sigma_max ** 2 / (1.0 * 1.0) 
    return eta_maxs

# Begin of graphics output
pylab.figure()
n, bins, patches = pylab.hist(eta_maxs, 100, histtype='step', cumulative=-1, 
                   log=True, normed=True, label="numerical evaluation of p_accept")
explaw = [math.exp( - 2.0 * (N - 1) * eta) for eta in bins]
pylab.plot(bins, explaw, 'r--', linewidth=1.5, label="1st order virial expansion")
pylab.xlabel('density')
pylab.ylabel('p_accept(density)')
pylab.legend()
pylab.show()
pylab.savefig('any.pdf')
