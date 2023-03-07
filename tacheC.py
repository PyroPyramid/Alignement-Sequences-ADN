from couts import *
import numpy as np


# Tache C
def DIST_2(x: str, y: str) -> int:
    """
    param x, y: deux mots

    return: distance d'édition entre x et y
    """

    n = len(x) + 1
    m = len(y) + 1
    l1 = np.arange(m) * cins()

    for i in range(1, n):

        l2 = np.zeros(m)
        l2[0] = i * cdel()

        for j in range(1, m):
            l2[j] = min(
                l2[j - 1] + cins(), l1[j] + cdel(), l1[j - 1] + csub(x[i - 1], y[j - 1])
            )

        l1 = l2

    return l2[len(y)]
