#!/usr/bin/python
## -*- coding: UTF-8 -*-

from Tkinter import *
import sys
import os
import re
import tweepy

#num_level = sys.argv[1]
num_score = sys.argv[1]

consumer_key = "deKFzlEcvVyxFKN8zLltG0O8Y"
consumer_secret = "V92ctEVIHK5LyM8GwpGk4tGK5Xo3gjle946RMCIRaxpAIz6v5N"
access_token = "2536799406-ch72qMsW98amMKPDZyfJfOU82wJB4c8P6Sgmg1U"
access_token_secret = "D34zTxwn6Uf7bS2bRHCVb4C8YTgMizDIFmPSaKLbXhM84"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

ventana = Tk()
ventana.title("Twitter")

# texto hacia la ventana
labell0 = Label(ventana, text = "Publica tu resultado en twitter")
labell0.grid(row = 1, column = 1)
labell0.pack()

# caja para ingresar el texto
texto1 = Label(ventana, text = "Nickname: @")
texto1.grid(row = 8, column=1)
texto1.pack()

username = StringVar() #variable que guarda el nick name 
caja = Entry(ventana, textvariable = username)
caja.grid(row = 8, column = 5)
caja.pack()

def tuitear1():
	Nick_Name = username.get()
	api.update_status('@'+ Nick_Name+' '+'ha alcanzado '+str(num_score) +' puntos jugando Fishbowl!')
	ventana.destroy()

def salir():
	ventana.destroy()

boton = Button(ventana, text = "Ingresar", command = tuitear1, bg = 'blue' ) #Boton que enviara el twit  
boton.grid(row = 15,column = 1)
boton.pack()

boton_exit = Button(ventana, text = "No tienes Twitter? Presiona para salir", command = salir, bg = 'green' )
boton_exit.grid(row = 25,column = 1)
boton_exit.pack()


ventana.mainloop()
