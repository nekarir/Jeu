import tkinter as tk
import numpy as np
from ttkbootstrap import Style


def button_click(btn, row, col):
    """Cette fonction prend en entrée le bouton, la ligne, la colonne, est utilisée lorsqu'un bouton est cliqué, elle met a jour l'interface graphique,
    lorsqu'un joueur appuie dessus le texte du bouton est changé, elle met donc à jour la matrice avec le coup du joueur.
    Elle passe aussi au joueur suivant en bloquant les boutons qui ont déjà été utilisés.
    Pour finir, elle vérifie si il y a un gagnant es elle affiche la fin du jeu."""
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
matrice = np.zeros([3, 3], dtype=np.int32)
joueur = 1


def get_input(joueur, matrice):
    """Cette fontion permet de récupérer les entrées des utilisateurs pour leur coup,
    de vérifier si la cellule choisie est vide. Elle prend en entrée la matrice et le joueur.
    Renvoie la matrice mise à jour avec le coup du joueur si celui-ci est validé."""
    input_ligne = int(input("Joueur "+str(joueur)+" tapez l'index de la ligne entre 0 et 2 : "))
    input_colonne = int(input("Joueur "+str(joueur)+" tapez l'index de la colonne entre 0 et 2 : "))
    if matrice[input_ligne, input_colonne] == 0:
        matrice[input_ligne, input_colonne] = joueur
        print(matrice)
        return matrice
    else:
        print("choisis une autre case")
        get_input(joueur, matrice)
        return matrice


def check_win(matrice):
    """Cette fonction permet de vérifier les conditions de victoire, d'égalité et s'il y a un tour suivant.
    Elle prend en entrée une matrice numpy 3 par 3. Et renvoie 0 si il y a un gagnant ou 1 si on passe
    au tour suivant. Lorsqu'il y a une victoire ou alors une égalité elle bloque la partie ainsi les joueurs ne peuvent plus jouer. """
    for i in range(matrice.shape[0]):
        if np.all(matrice[i, :] == 1):
            message_label.config(text="Le joueur A gagne avec une ligne")
            disable_buttons()
            return 0
        if np.all(matrice[i, :] == 2):
            message_label.config(text="Le joueur B gagne avec une ligne")
            disable_buttons()
            return 0
    for j in range(matrice.shape[1]):
        if np.all(matrice[:, j] == 1):
            message_label.config(text="Le joueur A gagne avec une colonne")
            disable_buttons()
            return 0
        if np.all(matrice[:, j] == 2):
            message_label.config(text="Le joueur B gagne avec une colonne")
            disable_buttons()
            return 0

    if np.all(np.diag(matrice) == 1):
        message_label.config(text="Le joueur A gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(matrice) == 2):
        message_label.config(text="Le joueur B gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(np.fliplr(matrice)) == 1):
        message_label.config(text="Le joueur A gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(np.diag(np.fliplr(matrice)) == 2):
        message_label.config(text="Le joueur B gagne avec une diagonale")
        disable_buttons()
        return 0
    if np.all(matrice != 0):
        message_label.config(text="Égalité")
        disable_buttons()
        return 0
    else:
        print("Tour suivant")
        return 1


def disable_buttons():
    """Cette fonction permet de désactiver tout les boutons du morpion.
    Elle ne prend pas d'entrées et ne renvoit rien"""
    for button in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]:
        button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Morpion")
style = Style(theme="flatly")

btn1 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn1, 0, 0))
btn1.grid(row=0, column=0, padx=3, pady=3)

btn2 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn2, 0, 1))
btn2.grid(row=0, column=1, padx=3, pady=3)

btn3 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn3, 0, 2))
btn3.grid(row=0, column=2, padx=3, pady=3)

btn4 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn4, 1, 0))
btn4.grid(row=1, column=0, padx=3, pady=3)

btn5 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn5, 1, 1))
btn5.grid(row=1, column=1, padx=3, pady=3)

btn6 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn6, 1, 2))
btn6.grid(row=1, column=2, padx=3, pady=3)

btn7 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn7, 2, 0))
btn7.grid(row=2, column=0, padx=3, pady=3)

btn8 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn8, 2, 1))
btn8.grid(row=2, column=1, padx=3, pady=3)

btn9 = tk.Button(root, width=15, height=6, text=" ", command=lambda: button_click(btn9, 2, 2))
btn9.grid(row=2, column=2, padx=3, pady=3)

message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.grid(row=3, columnspan=3)

root.mainloop()