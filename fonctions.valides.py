#!/usr/bin/env python3
# -*- coding: utf-8
"""
Created on Thu Apr  1 09:07:27 2021

@author: alban
"""
import tkinter as tk



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
length=300,width=20,label="nombre de points de nourriture",tickinterval=1,variable=nombre_point_nourriture)#,command=maj)
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

COTE = 1200
Canevas = tk.Canvas(fenetre,height=COTE,width=COTE,bg='white')
Canevas.grid(row = 0, column = 1, rowspan = 10, ipadx = 100, ipady = 100)

fenetre.mainloop()

