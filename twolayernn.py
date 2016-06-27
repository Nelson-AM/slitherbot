import numpy as np

# Sigmoid function
def nonlin(x, deriv = False):
    if deriv == True:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))

# Input dataset
x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# Output dataset
y = np.array([[0, 1, 1, 0]]).T

# Seed random numbers to make calculations (non?)deterministic.
np.random.seed(1)

# Initialize weights randomly with mean = 0.
syn0 = 2 * np.random.random((3, 1)) - 1


# 10k iterations
for iter in xrange(10):
    
    # Forward propagation
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))
    
    print l1
    
    # How much did we miss?
    l1_error = y - l1
    
    # Multipy the error by the slope of the sigmoid at the values in l1.
    l1_delta = l1_error * nonlin(l1, True)
    
    # Update weights
    syn0 += np.dot(l0.T, l1_delta)

print "Output after training: "
print l1
