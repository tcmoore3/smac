import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import ipdb

# list of neighbors for each square
neighbors =  [[1, 4, 0, 0], [2, 5, 0, 1], [3, 6, 1, 2], [3, 7, 2, 3],
             [5, 8, 4, 0], [6, 9, 4, 1], [7, 10, 5, 2], [7, 11, 6, 3],
             [9, 12, 8, 4], [10, 13, 8, 5], [11, 14, 9, 6], [11, 15, 10, 7],
             [13, 12, 12, 8], [14, 13, 12, 9], [15, 14, 13, 10], [15, 15, 14, 11]]

# initialize transfer matrix to zeroes
n = 4
transfer_matrix = np.zeros((n*n, n*n))

# now fill in transfer matrix with transfer probabilities
for i in range(n*n):
    for neighbor in range(4):
        transfer_matrix[neighbors[i][neighbor], i] += 0.25

# make sure transfer matrix is correct
for row in transfer_matrix:
    assert(np.sum(row)) == 1.0

# empty list for positions through time
positions_t = []

# positions at time 0 (start at top right square)
position = np.zeros(n*n)
position[-1] = 1

# find equilibrium probability vector
# this is the eigenvector associated with eigenvalue 1
eigenvalues, eigenvectors = np.linalg.eig(transfer_matrix)
eigenvalue_1 = np.where(np.abs(np.abs(eigenvalues) - 1.0) < 1e-8)[0][0]
print np.abs(eigenvectors[:, eigenvalue_1])
ipdb.set_trace()

# now loop through time and find the probability vector at time t
for step in range(100):
    print position
    positions_t.append(position)
    position = np.dot(transfer_matrix, position)
positions_t = np.asarray(positions_t)
ipdb.set_trace()
fig, ax = plt.subplots()
for p_square_t in positions_t.T:
    ax.plot(p_square_t[:31])
fig.savefig('figures/pebble_4x4.pdf')
