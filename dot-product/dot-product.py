import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    res = 0.0
    i = 0
    while(i<len(x)):
        res += x[i]*y[i]
        i += 1
    return res