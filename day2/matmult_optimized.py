
# Program to multiply two matrices using nested loops
import numpy as np

def matmult():
    N = 250

    # NxN matrix
    np.random.seed(0)
    X = np.random.randint(0,100, size=(N, N))

    # Nx(N+1) matrix
    np.random.seed(0)
    Y = np.random.randint(0,100, size=(N, N + 1))

    # Nx(N+1)
    result = np.zeros(shape=(N, N+1), dtype="int64")

    # iterate through rows of X
    for i in range(X.shape[0]):
        # iterate through columns of Y
        for j in range(Y.shape[1]):
            a = X[i, :]*Y[:, j]
            result[i, j] = a.sum()
            
    #for r in result:
    #print(r)
    
    return result
