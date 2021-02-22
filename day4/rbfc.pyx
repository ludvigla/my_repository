from math import exp
import numpy as np
cimport numpy as np
from scipy.interpolate import Rbf

ctypedef np.float_t DTYPE_t
def rbf_network_cythonized(np.ndarray[DTYPE_t, ndim=2] X, beta, theta):

    cdef int N, D, i, j, d
    cdef np.ndarray Y
    
    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j, d] - X[i, d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-(r * theta)**2)

    return Y

# Scipy implementation of a Radial Basis Function (RBF) approximation scheme
def rbf_scipy_cythonized(X, beta):

    cdef int N, D, i
    
    N = X.shape[0]
    D = X.shape[1]    
    rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    #Xtuple = tuple([X[:, i] for i in range(D)])
    Xtuple = tuple([X[:, i] for i in range(D)])

    return rbf(*Xtuple)