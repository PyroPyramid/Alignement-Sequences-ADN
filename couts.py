# Fonctions de couts
def cdel():
    return 2


def cins():
    return 2


def csub(a, b):
    if a == b:
        return 0

    elif {a, b} == {"A", "T"} or {a, b} == {"C", "G"}:
        return 3

    else:
        return 4


def csub_latin(a, b):
    V = {"A", "E", "I", "O", "U", "Y"}
    # utile pour la question 23

    if a == b:
        return 0

    elif (a in V and b in V) or (a not in V and b not in V):
        return 5

    else:
        return 7


def complementaire(x: str):
    """
    param x: caractère

    return: caractère de la paire concordante associé à x
    """
    if len(x) != 1:
        return
    if x == "A":
        return "T"
    if x == "T":
        return "A"
    if x == "C":
        return "G"
    return "C"
