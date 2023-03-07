import numpy as np
from couts import *

# Tache B
def DIST_1_aux(x: str, y: str):
    """ """
    n = len(x) + 1
    m = len(y) + 1
    # i et j vont de 0 à n et m inclus respectivement
    mat = np.zeros((n, m))

    mat[0, :] = np.arange(m) * cdel()
    mat[:, 0] = np.arange(n) * cins()

    for i in range(1, n):
        for j in range(1, m):
            mat[i, j] = min(
                mat[i, j - 1] + cins(),
                mat[i - 1, j] + cdel(),
                mat[i - 1, j - 1] + csub(x[i - 1], y[j - 1]),
            )

    return mat


def DIST_1(x: str, y: str) -> int:
    mat = DIST_1_aux(x, y)
    return mat[len(x)][len(y)]


def SOL_1(x: str, y: str, D: list) -> tuple[str, str]:
    n = len(x) + 1
    m = len(y) + 1
    i = n - 1
    j = m - 1
    (s, t) = ("", "")

    while D[i][j] > 0:
        if j > 0 and D[i][j] == D[i][j - 1] + cins():
            (s, t) = ("-" + s, y[j - 1] + t)
            j = j - 1

        elif i > 0 and D[i][j] == D[i - 1][j] + cdel():
            (s, t) = (x[i - 1] + s, "-" + t)
            i = i - 1

        elif D[i][j] == D[i - 1][j - 1] + csub(x[i - 1], y[j - 1]):
            (s, t) = (x[i - 1] + s, y[j - 1] + t)
            j = j - 1
            i = i - 1

    while i > 0:
        (s, t) = (x[i - 1] + s, y[i - 1] + t)
        i = i - 1

    return (s, t)


def PROG_DYN(x: str, y: str) -> tuple[int, tuple[str, str]]:
    mat = DIST_1_aux(x, y)
    return mat[len(x)][len(y)], SOL_1(x, y, mat)
