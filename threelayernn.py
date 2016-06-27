import numpy as np

# Sigmoid function
def nonlin(x, deriv = False):
    if deriv == True:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))

# Initialize input layer.
x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

# Initialize the output layer.
y = np.array([[0],
              [1],
              [1],
              [0]])

# np.random.seed(1)

# Initialize weights randomly with mean = 0.
syn0 = 2 * np.random.random((3, 4)) - 1
syn1 = 2 * np.random.random((4, 1)) - 1

for iter in xrange(60000):
    
    # Feed forward through layers 0, 1, and 2.
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    
    # Compute l2 error
    l2_error = y - l2
    
    if (iter % 10000) == 0:
        print "Error: " + str(np.mean(np.abs(l2_error)))
    
    # In what direction is the target value?
    l2_delta = l2_error * nonlin(l2, True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * nonlin(l1, True)
    
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)