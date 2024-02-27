import tkinter
import numpy
import numpy as np

x = np.zeros((3, 3))
x[0] = 1


def check_win(x):
    for i in range(x.shape[0]):
        if np.all(x[i, :] == 1):
            print("Le joueur A gagne avec une ligne")
        if np.all(x[i, :] == 2):
            print("Le joueur B gagne avec une ligne")
    for j in range(x.shape[1]):
        if np.all(x[:, j] == 1):
            print("Le joueur A gagne avec une colonne")
        if np.all(x[:, j] == 2):
            print("Le joueur B gagne avec une colonne")

    if np.all(np.diag(x) == 1):
        print("le joueur A gagne avec une diagonale")
    if np.all(np.diag(x) == 2):
        print("le joueur B gagne avec une diagonale")
    if np.all(np.diag(np.fliplr(x)) == 1):
        print("Le joueur A gagne avec une diagonale")
    if np.all(np.diag(np.fliplr(x)) == 2):
        print("Le joueur B gagne avec une diagonale")
    elif not np.all(x == 0):
        print("égalité")
    else:
        print('tour suivant')

check_win(x)
