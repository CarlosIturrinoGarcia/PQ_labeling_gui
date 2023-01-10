import numpy as np


def sig2matrix(sig):
    """"
    Create signal matrix for Training
    """
    siglength = len(sig)
    matcolumnsize = round(siglength / 18)
    num_classes = 6
    matrix = np.zeros((num_classes, matcolumnsize))
    return matrix


def conversion(region, matrix):
    """"
    Create the index in the signal matrix
    """
    region2matrix = round(region / 18)
    matrix[1, region2matrix] = 1
    print(np.shape(region))
    print(region)
