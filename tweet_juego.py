#!/usr/bin/python
## -*- coding: UTF-8 -*-
import sys
import os
import re
import tweepy

consumer_key = "deKFzlEcvVyxFKN8zLltG0O8Y"
consumer_secret = "V92ctEVIHK5LyM8GwpGk4tGK5Xo3gjle946RMCIRaxpAIz6v5N"
access_token = "2536799406-ch72qMsW98amMKPDZyfJfOU82wJB4c8P6Sgmg1U"
access_token_secret = "D34zTxwn6Uf7bS2bRHCVb4C8YTgMizDIFmPSaKLbXhM84"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tuitear(mensaje):
	if len(mensaje)>2:
		print "Twitteando: <<"+str(mensaje)+">>"
		api.update_status(mensaje)

try:
	nik_name = raw_input("Ingresa tu nik_name: @")

	msj = 'Has ganado la partida, gracias por usar nuestro juego!!!!! !:)'

	tuitear(str('@'+nik_name +' '+msj))

	print "twieet enviado!!!!!! :) "

except Exception, e:
	raise e 
	print"No hay internet"

