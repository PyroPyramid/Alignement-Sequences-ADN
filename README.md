# Alignement-Sequences-ADN
Projet d'algorithmique développé en Python dans le cadre d'une UE d'algorithmique suivie à Sorbonne Université, en L3.

Ayant 2 séquences d'ADN, on souhaite comparer leur similitude, et d'essayer de trouver l'alignement le plus probable pour que les 2 soient similaires, c'est-à-dire ayant la même taille et les mêmes génomes.

Pour aligner 2 séquences d'ADN, soit on insère un espace dans la première séquence, soit un espace dans la deuxième séquence, soit on échange un génome de la première séquence pour être le même que celui de la deuxième à la même position.

Pour cela, on a besoin de définir une fonction de coût. Celle-là est définie dans le fichier couts.py.

Le répertoire Instances_genome contient des instances de séquences d'ADN qu'on souhaite aligner.

Le fichier lecture_fichiers.py sert à lire ces instances.

Le fichier tacheA.py sert à mesurer la distance entre les 2 séquences, c'est-à-dire le coût minimal nécessaire pour les aligner. La fonction implémentée suit une méthode naïve récursive.

Le fichier tacheB.py contient une amélioration de la fonction de la tache A, mais aussi renvoie l'alignement optimal des 2 séquences, en utilisant une approche de programmation dynamique, et une matrice pour stocker les distances trouvées au fur et à mesure.

Le fichier tacheC.py contient une amélioration en termes de complexité spatiale de la fonction de calcul de distance de la tache B.

Le fichier tacheD.py permet de trouver l'alignement optimal des 2 séquences, en utilisant la fonction de la tache C et en suivant la méthode diviser pour régner.
