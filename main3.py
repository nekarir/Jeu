import numpy as np
from tkinter import *
import random

x = np.zeros((3, 3))

def check_win(x):
    '''Cette fonction permet de vérifier les conditions de victoire, d'égalité et s'il y a un tour suivant.
        Elle prend en entrée une matrice numpy 3 par 3. Et renvoie 0 si il y a un gagnant ou 1 si on passe au tour suivant'''
    for i in range(x.shape[0]):
        if np.all(x[i, :] == 1):
            print("Le joueur A gagne avec une ligne")
            return 0
        if np.all(x[i, :] == 2):
            print("L'IA gagne avec une ligne")
            return 0
    for j in range(x.shape[1]):
        if np.all(x[:, j] == 1):
            print("Le joueur A gagne avec une colonne")
            return 0
        if np.all(x[:, j] == 2):
            print("L'IA gagne avec une colonne")
            return 0

    if np.all(np.diag(x) == 1):
        print("le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(x) == 2):
        print("L'IA gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(x)) == 1):
        print("Le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(x)) == 2):
        print("L'IA gagne avec une diagonale")
        return 0
    if np.all(x != 0):
        print("Egalité")
        return 0
    else:
        print("Tour suivant")
        return 1


def get_input(joueur, x):
    '''Cette fontion permet de récupérer les entrées des utilisateurs pour leur coup,
        de vérifier si la cellule choisie est vide.
        Renvoie la matrice mise à jour avec le coup du joueur si celui-ci est validé.'''
    input_ligne = int(input("Joueur " + str(joueur) + " tapez l'index de la ligne entre 0 et 2 : "))
    input_colonne = int(input("Joueur " + str(joueur) + " tapez l'index de la colonne entre 0 et 2 : "))
    if x[input_ligne, input_colonne] == 0:
        x[input_ligne, input_colonne] = joueur
        print(x)
        return x
    else:
        print("choisis une autre case")
        get_input(joueur, x)
        return 0


def easy_ia(x, joueur):
    position = (random.randint(0, 2), random.randint(0, 2))



    while x[position[0], position[1]] != 0:
        position = (random.randint(0, 2), random.randint(0, 2))
    x[position[0], position[1]] = joueur
    print(x)
    return x

jeu = 1
matrice = np.zeros([3, 3], dtype=np.int32)
joueur = 1

while jeu == 1:
    if joueur == 1:
        matrice = get_input(joueur, matrice)
    else:
        matrice = easy_ia(matrice, joueur)

    jeu = check_win(matrice)

    if joueur == 1:
        joueur = 2
    else:
        joueur = 1


def ia_moyenne(matrice)
    ligne1 = matrice[0]
    ligne2 = matrice[1]
    ligne3 = matrice[2]
    colonne1 = matrice[:,0]
    colonne2 = matrice[:,1]
    colonne3 = matrice[:,2]

    diagonal = np.diag(matrice)
    diagonalinverse = np.fliplr(matrice)
    if np.array_equal(ligne1,[1,1,0]):
        return 0,2
    if np.array_equal(ligne1,[1,0,1]):
        return 0,1
    if np.array_equal(ligne1,[0,1,1]):
        return 0,0
    if np.array_equal(ligne2,[1,1,0]):
        return 1,2
    if np.array_equal(ligne2,[1,0,1]):
        return 1,1
    if np.array_equal(ligne2,[0,1,1]):
        return 1,0
    if np.array_equal(ligne3,[1,1,0]):
        return 2,2
    if np.array_equal(ligne3,[1,0,1]):
        return 2,1
    if np.array_equal(ligne3,[0,1,1]):
        return 2,0
    if np.array_equal(colonne1,[1,1,0]):
        return 2,0
    if np.array_equal(colonne1,[1,0,1]):
        return 1,0
    if np.array_equal(colonne1,[0,1,1]):
        return 0,0
    if np.array_equal(colonne2,[1,1,0]):
        return 2,1
    if np.array_equal(colonne2,[1,0,1]):
        return 1,1
    if np.array_equal(colonne2,[0,1,1]):
        return 0,1
    if np.array_equal(colonne3,[1,1,0]):
        return 2,2
    if np.array_equal(colonne3,[1,0,1]):
        return 1,2
    if np.array_equal(colonne3,[0,1,1]):
        return 0,2
