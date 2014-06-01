import pygame
import sys
import random
import os
import re
import tweepy
from pygame.locals import *
pygame.init()
pygame.font.init()

FPS = 30
frecuencia = pygame.time.Clock()
SCREEN = pygame.display.set_mode((960,720),0,32)
pygame.display.set_caption('FishBowl v0.5')


#Mouse
pygame.mouse.set_visible(False)
pygame.mouse.get_focused(True)
pygame.mouse.set_pos(430,360)

#Elementos generales
SCORE = 0
LEVEL = 1
CANTIDADALIMENTOS = 5

#Colores
LETRAS = (240,247,25)
NEGRO = (0,0,0)

#Elementos graficos
FONDO = pygame.image.load("back.jpg")
PEZ = pygame.image.load("fish")
PEZ2 = pygame.image.load("fish2")
PEZRECT = PEZ.get_rect
PEZD = pygame.image.load("fish_d")
ALIMENTO = pygame.image.load("food")
TEXTO = pygame.font.Font("Fishbowl.ttf",10)
textSurfaceObject = TEXTO.render("PUNTOS: " + str(SCORE) +"      NIVEL: " + str(LEVEL),True,LETRAS,NEGRO)
textRectObject = textSurfaceObject.get_rect()
textSurfaceObject2 = TEXTO.render("VICTORIA!",True,NEGRO,LETRAS)
textRectObject2 = textSurfaceObject.get_rect()
textRectObject2.center = (480,360)

#Alimentos
ALIMENTORECT = {}
ALIMENTOVISIBLE = {}
ALIMENTOX = 0
ALIMENTOY = 0
VELOCIDADY = {}
for iteracion in range(0,CANTIDADALIMENTOS): 
	ALIMENTORECT[iteracion] = ALIMENTO.get_rect()
	ALIMENTORECT[iteracion].left = random.randrange(0,960)
	ALIMENTORECT[iteracion].top = 0
	if LEVEL >1:
		CANTIDADALIMENTOS=CANTIDADALIMENTOS*LEVEL
	for iteracion2 in range(0,720) :
		ALIMENTORECT[iteracion].top = ALIMENTORECT[iteracion].top *200
		ALIMENTOVISIBLE[iteracion] = True

while True:
	SCREEN.blit(FONDO,(0,0)) #Colocacion fondo
	pygame.draw.line(SCREEN,NEGRO,(0,0),(960,0),50) #Barra superior
	SCREEN.blit(textSurfaceObject,textRectObject) #Coloca texto puntos con puntuacion
	for iteracion in range(0,CANTIDADALIMENTOS):
		if ALIMENTORECT[iteracion]:
			SCREEN.blit(ALIMENTO,ALIMENTORECT[iteracion])
			ALIMENTORECT[iteracion].move_ip(random.randrange(-2,2),random.randrange(0,3))

	for event in pygame.event.get():
		if event.type == QUIT:		
			pygame.quit()
			sys.exit()
		# Movimiento del Pez y orientacion
		(a,b)=pygame.mouse.get_pos() 
		if b<a:
			SCREEN.blit(PEZ2,(a,b))			
		if a<b:
			SCREEN.blit(PEZ,(a,b))	
		#for iteracion in range(0,CANTIDADALIMENTOS+1):
		#	if ALIMENTORECT[iteracion].collidepoint(a,b):
		#		SCORE = SCORE +1
		#		ALIMENTOVISIBLE[iteracion] = False
		#		if SCORE == CANTIDADALIMENTOS:
		#			LEVEL = LEVEL+1
		#			SCREEN.blit(textSurfaceObject2,textRectObject2)


	pygame.display.update()
	frecuencia.tick(FPS)


