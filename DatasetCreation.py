import numpy as np

def sig2matrix(sig):
    siglength = len(sig)
    matcolumnsize = round(siglength/18)
    return matcolumnsize

def conversion(region):
    print(np.shape(region))
    print(region)
