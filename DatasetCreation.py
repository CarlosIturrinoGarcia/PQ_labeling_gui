import numpy as np

def sig2matrix(sig):
    """"
    Create signal matrix for Training
    """
    siglength = len(sig)
    matcolumnsize = round(siglength/18)
    return matcolumnsize

def conversion(region):
    """"
    Create the index in the signal matrix
    """
    print(np.shape(region))
    print(region)
