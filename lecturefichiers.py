# Lecture de fichiers
def deleteSpaces(mot: str):
    """
    param mot: un mot avec ou sans espaces

    return: le même mot sans les espaces
    """

    res = ""

    for i in range(len(mot) - 1):
        if mot[i] != " ":
            res = res + mot[i]

    return res


def readADN(instance: str):
    """
    param instance: une instance d'ADN contenue dans le fichier "Instances_genome"

    return: taille de x, taille de y, mot x, mot y
    """
    file = open("Instances_genome/" + instance)
    n = int(file.readline())
    m = int(file.readline())
    x = deleteSpaces(file.readline())
    y = deleteSpaces(file.readline())

    return n, m, x, y
