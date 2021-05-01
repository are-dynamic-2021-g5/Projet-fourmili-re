#!/usr/bin/env python3
# -*- coding: utf-8
"""
Created on Thu Apr  1 09:07:27 2021

@author: alban
"""
import tkinter as tk
import numpy as np

import random
import math


fenetre=tk.Tk()
fenetre.title("fourmilière")


MAX=500
max_quantity_food = tk.StringVar()
max_quantity_food.set(MAX)
widget_max_quantity_food = tk.Scale(fenetre,from_=100,to=1000,resolution=25,orient=tk.HORIZONTAL,\
length=300,width=20,label="Quantité maximale de nourriture",tickinterval=100,variable=max_quantity_food)#,command=maj)
widget_max_quantity_food.grid(row = 0, column = 0)

NR=1
nombre_reine = tk.StringVar()
nombre_reine.set(NR)
widget_nombre_reine = tk.Scale(fenetre,from_=1,to=5,resolution=1,orient=tk.HORIZONTAL,\
length=300,width=20,label="Nombre de reines",tickinterval=1,variable=nombre_reine)#,command=maj)
widget_nombre_reine.grid(row = 1, column = 0)


NB=4
nombre_fourmi = tk.StringVar()
nombre_fourmi.set(NB)
widget_nombre_fourmi = tk.Scale(fenetre,from_=1,to=15,resolution=1,orient=tk.HORIZONTAL,\
length=300,width=20,label="Nombres fourmis",tickinterval=1,variable=nombre_fourmi)#,command=maj)
widget_nombre_fourmi.grid(row = 2, column = 0)

PN=1
nombre_point_nourriture = tk.StringVar()
nombre_point_nourriture.set(PN)
widget_nombre_point_nourriture = tk.Scale(fenetre,from_=1,to=10,resolution=1,orient=tk.HORIZONTAL,\
length=300,width=20,label="Nombre de points de nourriture",tickinterval=1,variable=nombre_point_nourriture)#,command=maj)
widget_nombre_point_nourriture.grid(row = 3, column = 0)


SPEED=10
speed = tk.StringVar()
speed.set(SPEED)
widget_speed = tk.Scale(fenetre,from_=0,to=30,resolution=1,orient=tk.HORIZONTAL,\
length=300,width=20,label="Vitesse",tickinterval=0.2,variable=speed)#,command=maj)
widget_speed.grid(row = 4, column = 0)


Label1 = tk.Label(fenetre, text = 'neigh', fg = 'black')
Label1.grid(row = 5, column = 0)
value =2
value = tk.StringVar() 
bouton1 = tk.Radiobutton(fenetre, text="1", variable=value, value=1)
bouton2 = tk.Radiobutton(fenetre, text="2", variable=value, value=2)
bouton3 = tk.Radiobutton(fenetre, text="3", variable=value, value=3)
bouton4 = tk.Radiobutton(fenetre, text="4", variable=value, value=4)
bouton1.grid(row = 6, column = 0)
bouton2.grid(row = 7, column = 0)
bouton3.grid(row = 8, column = 0)
bouton4.grid(row = 9, column = 0)

Arret = True

def Demarrer() :
    global Arret
    if Arret == True :
        Arret = False
        generate_simple_map(n,m)

BoutonGo = tk.Button(fenetre, text ='Démarrer', command = Demarrer)
BoutonGo.grid(row = 0, column = 3)
    
def Arreter() :
    global Arret
    Arret = True

BoutonArreter = tk.Button(fenetre, text ='Pause', command = Arreter())
BoutonArreter.grid(row = 1, column = 3)

def Reset() :
    global Arret
    Arret = True
    Canevas.delete(ALL)
    generate_simple_map(n,m)

BoutonReset = tk.Button(fenetre, text ='Reset', command = Reset)
BoutonReset.grid(row = 2, column = 3)

BoutonQuitter = tk.Button(fenetre, text ='Quitter', command = fenetre.destroy)
BoutonQuitter.grid(row = 3, column = 3)
COTE = 1200
Canevas = tk.Canvas(fenetre,height=COTE,width=COTE,bg='white')
Canevas.grid(row = 0, column = 1, rowspan = 10, ipadx = 100, ipady = 100)


c = 40
CN = []

                
n = m = 30 # nombre de lignes = nombre de colonnes
initial_size = 2 # taille de la fourmilière initiale
max_food_quantity = 500 #quantité maximale de nourriture par source de nourriture
neigh = 1 #voisinage / champ de vision de chaque fourmi


def generate_simple_map(n, m): # n : lignes m : colonnes
    """Préconditions : m > 0 et n > 0, initial_size > 0
    Renvoie un monde de taille n*m avec une fourmilière au centre et un point de nourriture en périphérie"""
    map = np.array([[" " for i in range(0, n)] for j in range(0, n)]) # on crée la matrice vide (avec des " " partout)
    # on crée la fourmilière au centre
    for i in range(0, initial_size):
        for k in range(0, initial_size):
            map = np.delete(map, m*(n//2 - initial_size//2 + i) + m//2 - initial_size//2 + k) #on copie le monde en enlevant une à une les cases du carré de taille initial_size situé au centre
            map = np.insert(map, m*(n//2 - initial_size//2 + i) + m//2 - initial_size//2 + k, "h") #on remplace les cases initialement vide (avec un " ") par une case "fourmilière" (avec un "h" pour "home")
            map = np.array([[map[m*j + i] for i in range(0, m)] for j in range(0, n) ])
    
    # on crée un point de nourriture
    food_line = random.randint(0, 2*n//5 - 1) # on définit ainsi la périphérie comme étant les cases du bord de la matrice avec un largeur de n/5
    food_column = random.randint(0, 2*m//5 - 1)
    if food_line > n//5 - 1: # on est sur la périphérie du bas
        food_line = n - 2 - n//5 + food_line
    if food_column > m//5 - 1: # on est sur la périphérie de droite
        food_column = m - 2 - m//5 + food_column
    where = random.sample([food_line, food_column], 1) # on définit une périphérie où se mettre (horizontale ou verticale)
    if where == food_line: # on est sur une périphérie en haut ou en bas
        food_column = random.randint(0, m - 1) # on définit une case au hasard sur cette périphérie
    else : #on est sur une périphérie latérale
        food_line = random.randint(0, n - 1) # on définit une case au hasard sur cette périphérie
    # on place dans la matrice de point de nourriture de quantité aléatoire food_quantity et de position périphérique aléatoire (food_line, food_column)
    food_quantity = random.randint(1, max_food_quantity) # on attribue à ce point de nourriture une certaine quantité de nourriture
    CN.append(([n,m],food_quantity))
    map = np.delete(map, m*food_line + food_column)
    map = np.insert(map, m*food_line + food_column, "c")
    map = np.array([[map[m*j + i] for i in range(0, m)] for j in range(0, n)] )       
    
    return map

def Affiche_Matrice(A):
    fenetre = tk.Tk()
    Text=str(A)
    l = tk.LabelFrame(fenetre, text="Notre matrice", padx=20, pady=20, width=600)
    l.pack(fill="both", expand="yes")
    tk.Label(l, text=Text).pack()
    fenetre.mainloop()

def spatial_neighborhood (map, a, b, neigh): #world : List[List[int]], a : int(ligne), b : int(colonne), neigh : int
    
    """Préconditions :0 <= a <= n-1  and 0 <= b <= m-1 and n >= 2*neigh and m >= 2*neigh
    Retourne la matrice des types des voisins de de l'individu en [a, b] avec a la ligne et b la colonne"""
    
    voisin = np.array([[" " for i in range(0, 2*neigh + 1)] for j in range(0, 2*neigh + 1)]) #grille vide de la taille du voisinage
    
    world_without_ind = np.delete(map, m*a + b) #on copie le monde sans l'individu
    world_without_ind = np.insert(world_without_ind, m*a + b, " ") #on remplace la place de l'individu par une case vide (avec un " ")
    world_without_ind = np.array([[world_without_ind[m*j + i] for i in range(0, m)] for j in range(0, n) ]) #on remet le monde sous forme de tableau
    

    if a - neigh >= 0 and a + neigh <= n - 1: # on teste les lignes, il n'y a pas de problème avec les bords (n-1 car les indices commencent à 0)
        if b - neigh >= 0 and b + neigh <= m - 1: #on teste les colonnes, il n'y a pas de problèmes avec les bords
            voisin = np.array([[world_without_ind[a-neigh + j, b-neigh + i] for i in range(0, 2*neigh + 1)] for j in range(0, 2*neigh + 1)]) 
        elif b - neigh < 0: # on atteint le bord gauche de la matrice
            voisin = np.array([[world_without_ind[a - neigh + j, i] for i in range(0, b + neigh + 1)] for j in range(0, 2*neigh + 1)])
        elif b + neigh > m - 1: # on atteint le bord droit
            voisin = np.array([[world_without_ind[a - neigh + j, i] for i in range(b - neigh, m)] for j in range(0, 2*neigh + 1)])
    elif a - neigh < 0 : # on atteint le bord haut
        if b - neigh >= 0 and b + neigh <= m - 1: #on teste les colonnes, il n'y a pas de problèmes avec les bords
            voisin = np.array([[world_without_ind[j, b-neigh + i] for i in range(0, 2*neigh + 1)] for j in range(0, a + neigh + 1)])
        elif b - neigh < 0: # on atteint le bord gauche de la matrice
            voisin = np.array([[world_without_ind[j, i] for i in range(0, b + neigh + 1)] for j in range(0, a + neigh + 1)])
        elif b + neigh > m - 1: # on atteint le bord droit
            voisin = np.array([[world_without_ind[j, i] for i in range(b - neigh, m)] for j in range(0, a + neigh + 1)])
    else : # a + neigh > n - 1
        if b - neigh >= 0 and b + neigh <= m - 1: #on teste les colonnes, il n'y a pas de problèmes avec les bords
            voisin = np.array([[world_without_ind[j, b-neigh + i] for i in range(0, 2*neigh + 1)] for j in range(a - neigh, n)]) #on copie 
        elif b - neigh < 0: # on atteint le bord gauche de la matrice
            voisin = np.array([[world_without_ind[j, i] for i in range(0, b + neigh + 1)] for j in range(a - neigh, n)])
        elif b + neigh > m - 1: # on atteint le bord droit
            voisin = np.array([[world_without_ind[j, i] for i in range(b - neigh, m)] for j in range(a - neigh, n)])
    return voisin



    
def ants (map, nb_ants):
    """Precondition : nb_ants >= 0
    Fait apparaitre nb_ants fourmis autour de la fourmilière"""
    ants_map = map
    for k in range(0, n):
        for l in range(0, m):
            if ants_map[k, l] == " ": #on vérifie que la case est vide
                for o in spatial_neighborhood(map, k, l, neigh):
                    for p in o:
                        if p == "h" and nb_ants > 0 : #on regarde si il y a une case fourmilière dans le voisinage
                            if ants_map[k, l] == " ": #on vérifie que la case est vide
                                ants_map = np.delete(ants_map, m*k + l) #on copie le monde en enlevant la case ayant la fourmilière pour voisin
                                ants_map = np.insert(ants_map, m*k + l, "f") #on remplace les cases initialement vide (avec un 0) par une case "fourmi" (avec un 2)
                                ants_map = np.array([[ants_map[m*j + i] for i in range(0, m)] for j in range(0, n) ])
                                nb_ants = nb_ants - 1
    q = 0                            
    while nb_ants > 0: #la fourmilière est entourée de fourmis
        q = q + 1
        for k in range(0, n):
            for l in range(0, m):
                if ants_map[k, l] == " ": #on vérifie que la case est vide
                    for o in spatial_neighborhood(map, k, l, neigh + q):
                        for p in o:
                            if p == "h" and nb_ants > 0 : #on regarde si il y a une case fourmilière dans le voisinage + q
                                if ants_map[k, l] == " ": #on vérifie que la case est vide
                                    ants_map = np.delete(ants_map, m*k + l) #on copie le monde en enlevant la case ayant la fourmilière pour voisin
                                    ants_map = np.insert(ants_map, m*k + l, "f") #on remplace les cases initialement vide (avec un " ") par une case "fourmi" (avec un f)
                                    ants_map = np.array([[ants_map[m*j + i] for i in range(0, m)] for j in range(0, n) ])
                                    nb_ants = nb_ants - 1                        
    return ants_map






def np_into_tk_fourmi(l):
    """Affiche un tableau nupy sur tkinter"""
    for i in range(0, len(l)) :
        for j in range(0, len(l[0])) :
            if l[i][j] == 'h' :
                Canevas.create_rectangle(j*c, COTE-i*c,j*c+c,COTE -i*c -c,outline='purple', fill='purple')
            elif l[i][j] == 'f': 
                Canevas.create_rectangle(j*c, COTE-i*c,j*c+c,COTE -i*c -c,outline='blue', fill='blue')
          
            elif l[i][j]=='c' :
                Canevas.create_rectangle(j*c, COTE-i*c,j*c+c,COTE -i*c -c,outline='green' , fill='green')

Canevas.create_line(COTE,0,COTE,COTE,0,COTE, fill='black')
np_into_tk_fourmi(k)
fenetre.mainloop()