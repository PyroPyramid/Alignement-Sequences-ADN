from couts import *

def dist_naif_rec(x: str, y: str, i: int, j: int, c: int, dist: int) -> int:
    """
    param x, y: deux mots
    param i, j: deux indices resp. dans [0..|x|] et [0..|y|]
    param c: coût de l'alignement de (x[1:i], y[1:j])
    param dist: le côut du meilleur alignement de (x,y) connu après cet appel

    return: distance d'édition entre x et y
    """
    if i == len(x) and j == len(y):  # cas final : coût du meilleur alignement
        if c < dist:
            dist = c

    else:  # cas récursif : on augmente soit i soit j soit les deux et on cherche le coût minimal
        if i < len(x) and j < len(y):  # on a pas fini de parcourir x et y "+" on est sur un cas de substitution : changer une lettre de x en une lettre de y, est encodée par deux lettres différentes dans x barre et y barre
            dist = dist_naif_rec(x, y, i + 1, j + 1, c + csub(x[i], y[j]), dist)

        if i < len(x):  # on a pas fini de parcourir x "+" on est sur un cas de suppression
            dist = dist_naif_rec(x, y, i + 1, j, c + cdel(), dist)

        if j < len(y):  # on a pas fini de parcourir y "+" on est sur un cas d'insertion
            dist = dist_naif_rec(x, y, i, j + 1, c + cins(), dist)
    return dist


def dist_naif(x: str, y: str) -> int:
    """
    param x, y: deux mots

    return: distance d'édition entre x et y
    """
    return dist_naif_rec(x, y, 0, 0, 0, float("inf"))
