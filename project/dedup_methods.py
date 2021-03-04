def edit_dist(a, b):
    """

    Edit distance

    Returns the edit distance/hamming distances between 
    two strings of equal length.

    Parameters
    ----------
    a, b : str
    	UMI string. Lengths of a and b have to be equal.

    Returns
    ----------
    int
        hamming distance

    """

    assert len(a) == len(b)
    dist = sum([not a == b for a, b in zip(a, b)])
    return dist