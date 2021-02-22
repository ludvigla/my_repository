def simple_add(a,b):
    """
    The sum of two numbers.
    
    Parameters
    ----------
    a, b : int or float
    
    Returns
    ----------
    int
        sum of `a` and `b`.

    """
    return a+b

def simple_sub(a,b):
    """
    The subtraction of two numbers.
    
    Parameters
    ----------
    a, b : int or float
    
    Returns
    ----------
    int
        `b` subtracted from `a`

    """
    return a-b

def simple_mult(a,b):
    """
    The product of two numbers.
    
    Parameters
    ----------
    a, b : int or float
    
    Returns
    ----------
    int
        `a` times `b`

    """
    return a*b

def simple_div(a,b):
    """
    The division of two numbers.
    
    Parameters
    ----------
    a, b : int or float
    
    Returns
    ----------
    int
        `a` divided by `b`

    """
    return a/b

def poly_first(x, a0, a1):
    """
    First degree polynomial.
    
    Parameters
    ----------
    x : array_like
        1d array containing data with float or int type
    a0, a1 : int or float
    
    Returns
    ----------
    array_like
        1d array with first degree polynomial `a0 + a1*x`

    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Second degree polynomial.
    
    Parameters
    ----------
    x : array_like
        1d array containing data with float or int type
    a0, a1, a2 : int or float
    
    Returns
    ----------
    array_like
        1d array with second degree polynomial `a0 + a1*x + a2*x**2`

    """
    return poly_first(x, a0, a1) + a2*(x**2)
