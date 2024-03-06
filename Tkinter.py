import tkinter as tk
import numpy as np
from tkinter import *
from tkinter.ttk import *
import random
from ttkbootstrap import Style
import random
def button_click(btn, row, col):
    global joueur
    global matrice
    btn.config(text="X" if joueur == 1 else "O", state=tk.DISABLED)
    matrice[row, col] = joueur

    jeu = check_win(matrice)
    if jeu == 0:
        print("Fin du jeu.")
        return

    joueur = 2 if joueur == 1 else 1

global joueur
global matrice
matrice = np.zeros([3,3],dtype=np.int32)
joueur = 1


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

def check_win(x):
    '''Cette fonction permet de vérifier les conditions de victoire, d'égalité et s'il y a un tour suivant.
    Elle prend en entrée une matrice numpy 3 par 3. Et renvoie 0 si il y a un gagnant ou 1 si on passe au tour suivant'''
    for i in range(x.shape[0]):
        if np.all(x[i, :] == 1):
            message_label.config(text="Le joueur A gagne avec une ligne")
            disable_buttons()
            return 0
        if np.all(x[i, :] == 2):
            message_label.config(text="Le joueur B gagne avec une ligne")
            disable_buttons()
            return 0
    for j in range(x.shape[1]):
        if np.all(x[:, j] == 1):
            message_label.config(text="Le joueur A gagne avec une colonne")
            disable_buttons()
            return 0
        if np.all(x[:, j] == 2):
            message_label.config(text="Le joueur B gagne avec une colonne")
            disable_buttons()
            return 0

    if np.all(np.diag(x) == 1):
        message_label.config(text="Le joueur A gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(x) == 2):
        message_label.config(text="Le joueur B gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(np.fliplr(x)) == 1):
        message_label.config(text="Le joueur A gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(np.fliplr(x)) == 2):
        message_label.config(text="Le joueur B gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(x != 0):
        message_label.config(text="égalité")
        disable_buttons()
        return 0
    else:
        print("tour suivant")
        return 1

def disable_buttons():
    for button in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Morpion")
style = Style(theme="flatly")

btn1 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn1, 0, 0))
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn2, 0, 1))
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn3, 0, 2))
btn3.grid(row=0, column=2, padx=5, pady=5)

btn4 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn4, 1, 0))
btn4.grid(row=1, column=0, padx=5, pady=5)

btn5 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn5, 1, 1))
btn5.grid(row=1, column=1, padx=5, pady=5)

btn6 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn6, 1, 2))
btn6.grid(row=1, column=2, padx=5, pady=5)

btn7 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn7, 2, 0))
btn7.grid(row=2, column=0, padx=5, pady=5)

btn8 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn8, 2, 1))
btn8.grid(row=2, column=1, padx=5, pady=5)

btn9 = tk.Button(root, width=30, height=12, text=" ", command=lambda: button_click(btn9, 2, 2))
btn9.grid(row=2, column=2, padx=5, pady=5)

message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.grid(row=3, columnspan=3)

def medium_ia(joueur, matrice):
    ligne1 = matrice[0]
    ligne2 = matrice[1]
    ligne3 = matrice[2]
    colonne1 = matrice[:, 0]
    colonne2 = matrice[:, 1]
    colonne3 = matrice[:, 2]

    diagonal = np.diag(matrice)
    diagonalinverse = np.diag(np.fliplr(matrice))

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

root.mainloop()