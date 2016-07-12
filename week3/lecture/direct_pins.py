import matplotlib as mpl
mpl.use('Agg')
import random
import numpy as np
import matplotlib.pyplot as plt

N = 15
L = 10.0
sigma = 0.1
n_configs = 10000
all_configs = np.empty((n_configs, N))
for config in range(n_configs):
    x = []
    while len(x) < N:
        x.append(random.uniform(sigma, L - sigma))
        for k in range(len(x) - 1):
            if abs(x[-1] - x[k]) < 2.0 * sigma:
                x = []
                break
    all_configs[config] = np.asarray(x)
    #print x
import ipdb
hist, bins = np.histogram(all_configs, bins=100, normed=True)
fig, ax = plt.subplots()
ax.plot(bins[:-1], hist)
fig.savefig('figures/hist.pdf')
