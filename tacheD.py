from couts import *
import numpy as np


# Tache D
def mot_gaps(k: int) -> str:
    """
    param k: entier

    return: mot composé de k gaps
    """

    return k * "-"


def align_lettre_mot(x: str, y: str) -> tuple[str, str]:
    """
    param x: mot de longueur 1
    param y: mot non vide, de longueur quelconque

    return: meilleur alignement de (x,y)
    """

    if (len(x) != 1) or (len(y) == 0):
        return ("","")

    ali_x = list(mot_gaps(len(y)))
    tmp = -1

    for i in range(len(y)):

        if y[i] == x:
            ali_x[i] = x
            return "".join(ali_x), y

        if y[i] == complementaire(x):
            tmp = i

    if tmp == -1:
        return x.join(ali_x), "-".join(y)

    ali_x[tmp] = x
    return "".join(ali_x), y


def coupure(x: str, y: str) -> int:
    """
    param x, y: deux mots

    return: indice de la coupure dans y (associée à l'indice |x|/2 dans x)
    """

    c = len(x) // 2
    n = len(x) + 1
    m = len(y) + 1

    l1 = np.arange(m) * cins()
    p1 = np.arange(m)

    for i in range(1, c + 1):

        l2 = np.zeros(m)
        l2[0] = i * cdel()

        for j in range(1, m):

            l2[j] = min(
                l2[j - 1] + cins(), l1[j] + cdel(), l1[j - 1] + csub(x[i - 1], y[j - 1])
            )

        l1 = l2

    for i in range(c + 1, n):

        l2 = np.zeros(m)
        l2[0] = i * cdel()
        p2 = np.zeros(m)

        for j in range(1, m):
            dict = {
                p2[j - 1]: l2[j - 1] + cins(),
                p1[j]: l1[j] + cdel(),
                p1[j - 1]: l1[j - 1] + csub(x[i - 1], y[j - 1]),
            }

            l2[j] = min(
                l2[j - 1] + cins(), l1[j] + cdel(), l1[j - 1] + csub(x[i - 1], y[j - 1])
            )

            p2[j] = min(dict, key=dict.get)
            del dict

        p1 = p2
        l1 = l2

    return int(p2[len(y)])


def SOL_2(x: str, y: str) -> tuple[str, str]:
    """
    param x, y: deux mots

    return: alignement de coût minimal entre x et y
    """

    # cas |y|=0 -> mot vide
    if len(y) < 1:
        return (x, mot_gaps(len(x)))

    # cas |x|=0
    if len(x) < 1:
        return (mot_gaps(len(y)), y)

    if len(x) < 2:
        return align_lettre_mot(x, y)

    # récurence :
    i1 = len(x) // 2
    i2 = coupure(x, y)
    s1, t1 = SOL_2(x[0:i1], y[0:i2])
    s2, t2 = SOL_2(x[i1 : len(x)], y[i2 : len(y)])

    return s1 + s2, t1 + t2
