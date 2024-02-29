import tkinter
import numpy
from tkinter import *
import numpy as np

x = np.zeros((3,3))

def check_win(x):
    '''Cette fonction permet de vérifier les conditions de victoire, d'égalité et s'il y a un tour suivant.
    Elle prend en entrée une matrice numpy 3 par 3. Et renvoie 0 si il y a un gagnant ou 1 si on passe au tour suivant'''
    for i in range(x.shape[0]):
        if np.all(x[i, :] == 1):
            print("Le joueur A gagne avec une ligne")
            return 0
        if np.all(x[i, :] == 2):
            print("Le joueur B gagne avec une ligne")
            return 0
    for j in range(x.shape[1]):
        if np.all(x[:, j] == 1):
            print("Le joueur A gagne avec une colonne")
            return 0
        if np.all(x[:, j] == 2):
            print("Le joueur B gagne avec une colonne")
            return 0

    if np.all(np.diag(x) == 1):
        print("le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(x) == 2):
        print("le joueur B gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(x)) == 1):
        print("Le joueur A gagne avec une diagonale")
        return 0
    if np.all(np.diag(np.fliplr(x)) == 2):
        print("Le joueur B gagne avec une diagonale")
        return 0
    if np.all(x == 0):
        print("égalité")
        return 0
    else:
        print("tour suivant")
        return 1


def get_input(joueur,x):
    '''Cette fontion permet de récupérer les entrées des utilisateurs pour leur coup,
    de vérifier si la cellule choisie est vide.
    Renvoie la matrice mise à jour avec le coup du joueur si celui-ci est validé.'''
    input_ligne = int(input("Joueur "+str(joueur)+" tapez l'index de la ligne entre 0 et 2 : "))
    input_colonne = int(input("Joueur "+str(joueur)+" tapez l'index de la colonne entre 0 et 2 : "))
    if x[input_ligne, input_colonne] == 0:
        x[input_ligne, input_colonne] = joueur
        print(x)
        return x
    else:
        print("choisis une autre case")
        get_input(joueur,x)
        return x


jeu = 1
matrice = np.zeros([3,3],dtype=np.int32)
joueur = 1

while jeu == 1:
    matrice = get_input(joueur,matrice)
    jeu = check_win(matrice)
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1