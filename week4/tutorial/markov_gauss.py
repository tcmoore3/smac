import matplotlib as mpl
mpl.use('Agg')
import random, math
import matplotlib.pyplot as plt
import numpy as np

x = 0.0
delta = 0.5
N_samples = 100000
sampled = np.empty(N_samples)
for k in range(N_samples):
    x_new = x + random.uniform(-delta, delta)
    if random.uniform(0.0, 1.0) <  \
         math.exp (- x_new ** 2 / 2.0) / math.exp (- x ** 2 / 2.0): 
        x = x_new 
    #print x
    sampled[k] = x
fig, ax = plt.subplots()
ax.hist(sampled, bins='auto')
fig.savefig('figures/markov-gauss.pdf')
