import numpy as np
import random

matrice = np.zeros((3, 3), dtype=np.int32)


def check_win(matrice):
    for i in range(matrice.shape[0]):
        if np.all(matrice[i, :] == 1):
            print("Le joueur A gagne avec une ligne")
            return 0
        if np.all(matrice[i, :] == 2):
            print("Le joueur B gagne avec une ligne")
            return 0
    for j in range(matrice.shape[1]):
        if np.all(matrice[:, j] == 1):
            print("Le joueur A gagne avec une colonne")
            return 0
        if np.all(matrice[:, j] == 2):
            print("Le joueur B gagne avec une colonne")
            return 0

    if np.all(np.diag(matrice) == 1):
        print("le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(matrice) == 2):
        print("le joueur B gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(matrice)) == 1):
        print("Le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(matrice)) == 2):
        print("Le joueur B gagne avec une diagonale")
        return 0
    if np.all(matrice != 0):
        print("Égalité")
        return 0
    else:
        print("tour suivant")
        return 1


def get_input(joueur, matrice):
    input_ligne = int(input("Joueur " + str(joueur) + " tapez l'index de la ligne entre 0 et 2 : "))
    input_colonne = int(input("Joueur " + str(joueur) + " tapez l'index de la colonne entre 0 et 2 : "))
    if matrice[input_ligne, input_colonne] == 0:
        matrice[input_ligne, input_colonne] = joueur
        print(matrice)
        print(joueur)
        return matrice
    else:
        print("choisis une autre case")
        return get_input(joueur, matrice)


def hard_ia(joueur, matrice):
    ligne1 = matrice[0]
    ligne2 = matrice[1]
    ligne3 = matrice[2]
    colonne1 = matrice[:, 0]
    colonne2 = matrice[:, 1]
    colonne3 = matrice[:, 2]

    diagonal = np.diag(matrice)
    diagonalinverse = np.diag(np.fliplr(matrice))

    if np.array_equal(ligne1, [2, 2, 0]):
        return 0, 2
    if np.array_equal(ligne1, [2, 0, 2]):
        return 0, 1
    if np.array_equal(ligne1, [0, 2, 2]):
        return 0, 0
    if np.array_equal(ligne2, [2, 2, 0]):
        return 1, 2
    if np.array_equal(ligne2, [2, 0, 2]):
        return 1, 1
    if np.array_equal(ligne2, [0, 2, 2]):
        return 1, 0
    if np.array_equal(ligne3, [2, 2, 0]):
        return 2, 2
    if np.array_equal(ligne3, [2, 0, 2]):
        return 2, 1
    if np.array_equal(ligne3, [0, 2, 2]):
        return 2, 0
    if np.array_equal(colonne1, [2, 2, 0]):
        return 2, 0
    if np.array_equal(colonne1, [2, 0, 2]):
        return 1, 0
    if np.array_equal(colonne1, [0, 2, 2]):
        return 0, 0
    if np.array_equal(colonne2, [2, 2, 0]):
        return 2, 1
    if np.array_equal(colonne2, [2, 0, 2]):
        return 1, 1
    if np.array_equal(colonne2, [0, 2, 2]):
        return 0, 1
    if np.array_equal(colonne3, [2, 2, 0]):
        return 2, 2
    if np.array_equal(colonne3, [2, 0, 2]):
        return 1, 2
    if np.array_equal(colonne3, [0, 2, 2]):
        return 0, 2
    if np.array_equal(diagonal, [2, 2, 0]):
        return 2, 2
    if np.array_equal(diagonal, [2, 0, 2]):
        return 1, 1
    if np.array_equal(diagonal, [0, 2, 2]):
        return 0, 0
    if np.array_equal(diagonalinverse, [2, 2, 0]):
        return 2, 0
    if np.array_equal(diagonalinverse, [2, 0, 2]):
        return 1, 1
    if np.array_equal(diagonalinverse, [0, 2, 2]):
        return 0, 2
    if np.array_equal(ligne1, [1, 1, 0]):
        return 0, 2
    if np.array_equal(ligne1, [1, 0, 1]):
        return 0, 1
    if np.array_equal(ligne1, [0, 1, 1]):
        return 0, 0
    if np.array_equal(ligne2, [1, 1, 0]):
        return 1, 2
    if np.array_equal(ligne2, [1, 0, 1]):
        return 1, 1
    if np.array_equal(ligne2, [0, 1, 1]):
        return 1, 0
    if np.array_equal(ligne3, [1, 1, 0]):
        return 2, 2
    if np.array_equal(ligne3, [1, 0, 1]):
        return 2, 1
    if np.array_equal(ligne3, [0, 1, 1]):
        return 2, 0
    if np.array_equal(colonne1, [1, 1, 0]):
        return 2, 0
    if np.array_equal(colonne1, [1, 0, 1]):
        return 1, 0
    if np.array_equal(colonne1, [0, 1, 1]):
        return 0, 0
    if np.array_equal(colonne2, [1, 1, 0]):
        return 2, 1
    if np.array_equal(colonne2, [1, 0, 1]):
        return 1, 1
    if np.array_equal(colonne2, [0, 1, 1]):
        return 0, 1
    if np.array_equal(colonne3, [1, 1, 0]):
        return 2, 2
    if np.array_equal(colonne3, [1, 0, 1]):
        return 1, 2
    if np.array_equal(colonne3, [0, 1, 1]):
        return 0, 2
    if np.array_equal(diagonal, [1, 1, 0]):
        return 2, 2
    if np.array_equal(diagonal, [1, 0, 1]):
        return 1, 1
    if np.array_equal(diagonal, [0, 1, 1]):
        return 0, 0
    if np.array_equal(diagonalinverse, [1, 1, 0]):
        return 2, 0
    if np.array_equal(diagonalinverse, [1, 0, 1]):
        return 1, 1
    if np.array_equal(diagonalinverse, [0, 1, 1]):
        return 0, 2
    position = (random.randint(0, 2), random.randint(0, 2))
    while matrice[position[0], position[1]] != 0:
        position = (random.randint(0, 2), random.randint(0, 2))
    matrice[position[0], position[1]] = joueur
    return position


jeu = 1
joueur = 1

while jeu == 1:
    if joueur == 1:
        matrice = get_input(joueur, matrice)
    else:
        position = hard_ia(joueur, matrice)
        matrice[position[0], position[1]] = joueur
        print(matrice)

    jeu = check_win(matrice)

    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
