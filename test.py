from tacheA import *
from tacheB import *
from tacheC import *
from tacheD import *
from lecturefichiers import *
from os import listdir
from os.path import isfile, join
import time


# TESTS TACHE A


def test_dist_naif():
    # test instances 44, 7 et 8 pour dist_naif()

    (n,m,x,y) = readADN("Inst_0000010_44.adn")
    assert(dist_naif(x,y) == 10)

    (n,m,x,y) = readADN("Inst_0000010_7.adn")
    assert(dist_naif(x,y) == 8)

    (n,m,x,y) = readADN("Inst_0000010_8.adn")
    assert(dist_naif(x,y) == 2)


#TESTS TACHE B

def test_DIST_1():
    (n,m,x,y) = readADN("Inst_0000010_44.adn")
    assert(DIST_1(x,y) == 10)

    (n,m,x,y) = readADN("Inst_0000010_7.adn")
    assert(DIST_1(x,y) == 8)

    (n,m,x,y) = readADN("Inst_0000010_8.adn")
    assert(DIST_1(x,y) == 2)


def test_PROG_DYN():
    (n,m,x,y) = readADN("Inst_0000010_7.adn")
    (d, (a1,a2)) = PROG_DYN(x,y)
    print("Instance = " + "Inst_0000010_7.adn" + ", distance = " + str(d) + ", alignement: " + a1 + ", " + a2)
    (n,m,x,y) = readADN("Inst_0000010_8.adn")
    (d, (a1,a2)) = PROG_DYN(x,y)
    print("Instance = " + "Inst_0000010_8.adn" + ", distance = " + str(d) + ", alignement: " + a1 + ", " + a2)
    (n,m,x,y) = readADN("Inst_0000010_44.adn")
    (d, (a1,a2)) = PROG_DYN(x,y)
    print("Instance = " + "Inst_0000010_44.adn" + ", distance = " + str(d) + ", alignement: " + a1 + ", " + a2)



#TESTS TACHE C
def test_DIST_2():
    fichiers = [f for f in listdir("Instances_genome") if isfile(join("Instances_genome", f))]
    fichiers.sort()

    for i in range(40):
        file = fichiers[i]
        (n,m,x,y) = readADN(file)
        assert(DIST_1(x,y) == DIST_2(x,y))
        print(n)

    

#TESTS TACHE D
def test_SOL_2():
    (n,m,x,y) = readADN("Inst_0000010_7.adn")
    (a1,a2) = SOL_2(x,y)
    assert((a1,a2) == ("TGGGTG--CTAT", "-GGG-GTTCTAT"))
    (n,m,x,y) = readADN("Inst_0000010_8.adn")
    (a1,a2) = SOL_2(x,y)
    assert((a1,a2) == ("AACTGTCTTT", "AACTGT-TTT"))
    (n,m,x,y) = readADN("Inst_0000010_44.adn")
    (a1,a2) = SOL_2(x,y)
    assert((a1,a2) == ("TATATGAGTC", "TAT-T---T-"))


test_dist_naif()
test_DIST_1()
test_PROG_DYN()
test_DIST_2()
test_SOL_2()
