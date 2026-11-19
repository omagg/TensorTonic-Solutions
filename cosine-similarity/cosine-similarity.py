import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    res = 0.0
    i = 0
    while(i < len(a)):
        res += a[i]*b[i]
        i += 1

    a_norm = 0
    for item in a:
        a_norm += item**2

    a_norm = a_norm**0.5
    if a_norm==0:
        return 0.0

    b_norm = 0
    for item in b:
        b_norm += item**2

    b_norm = b_norm**0.5
    if b_norm==0:
        return 0.0

    final_res = res/(a_norm*b_norm)

    return final_res