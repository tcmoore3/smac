
# coding: utf-8

# In[77]:

import random
from collections import OrderedDict


# In[150]:

def markov(x0, sigma, delta, n_steps, reference_configurations, del_xy=0.1):
    """
    Perform markov sampling of hard disks
    
    x0: the initial configuration
    sigma: the radius of the disks
    delta: the maximum step size in any direction
    n_steps: the number of steps to run
    """
    if x0 == None:
        x0 = [[0.25, 0.25], [0.75, 0.25], [0.25, 0.75], [0.75, 0.75]]
    sigma_sq = sigma ** 2
    for steps in range(n_steps):
        a = random.choice(x0)
        b = [a[0] + random.uniform(-delta, delta), a[1] + random.uniform(-delta, delta)]
        min_dist = min((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2 for c in x0 if c != a)
        box_cond = min(b[0], b[1]) < sigma or max(b[0], b[1]) > 1.0 - sigma
        if not (box_cond or min_dist < 4.0 * sigma ** 2): 
            a[:] = b
        # now check for overlap; this adds to the counter
        reference_configurations = check_overlap(x0, reference_configurations, del_xy)
    return x0, reference_configurations
            
def check_overlap(x_vec, reference_configurations, del_xy):
    for reference_configuration, d in reference_configurations.iteritems():
        condition_hit = True
        for b in d['configuration']:
            condition_b = min(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a in x_vec) < del_xy
            condition_hit *= condition_b
        d['hits'] += condition_hit
    return reference_configurations
        
def initialize_reference_configurations():
    conf_a = ((0.30, 0.30), (0.30, 0.70), (0.70, 0.30), (0.70,0.70))
    conf_b = ((0.20, 0.20), (0.20, 0.80), (0.75, 0.25), (0.75,0.75))
    conf_c = ((0.30, 0.20), (0.30, 0.80), (0.70, 0.20), (0.70,0.70))
    counter = OrderedDict([(letter, {'configuration': conf, 'hits': 0}) for letter, conf in zip(
        ['a', 'b', 'c'], [conf_a, conf_b, conf_c])])
    return counter


# In[166]:

for n_steps in [10000, 100000, 1000000, 10000000]:
    print n_steps, 'steps'
    print '--------------'
    total_hits = {'a': 0, 'b': 0, 'c': 0}
    for i in range(3):
        reference_configurations = initialize_reference_configurations()
        x, total = markov(None, 0.15, 0.1, n_steps,
                        reference_configurations, del_xy=0.1)
        for c, d in reference_configurations.iteritems():
            total_hits[c] += d['hits']
        a = reference_configurations
        print a['a']['hits'], a['b']['hits'], a['c']['hits']
    print total_hits['a']/3.0, total_hits['b']/3.0, total_hits['c']/3.0
    print ''

