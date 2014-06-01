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
pygame.display.set_caption('FishBowl v0.3')


#Mouse
pygame.mouse.set_visible(False)
pygame.mouse.get_focused(True)
pygame.mouse.set_pos(430,360)

#Elementos generales
SCORE = 0
CANTIDADALIMENTOS = 10

#Colores
LETRAS = (240,247,25)
NEGRO = (0,0,0)

#Elementos graficos
FONDO = pygame.image.load("back.jpg")
PEZ = pygame.image.load("fish")
PEZRECT = PEZ.get_rect
PEZD = pygame.image.load("fish_d")
ALIMENTO = pygame.image.load("food")
TEXTO = pygame.font.Font("Fishbowl.ttf",10)
textSurfaceObject = TEXTO.render("PUNTOS: " + str(SCORE),True,LETRAS,NEGRO)
textRectObject = textSurfaceObject.get_rect()

#Alimentos
ALIMENTORECT = {}
ALIMENTOVISIBLE = {}
ALIMENTOX = 0
ALIMENTOY = 0
VELOCIDADY = {}
for iteracion in range(0,CANTIDADALIMENTOS+1): 
	ALIMENTORECT[iteracion] = ALIMENTO.get_rect()
	ALIMENTORECT[iteracion].left = random.randrange(0,960)
	ALIMENTORECT[iteracion].top = 0
	for iteracion2 in range(0,720) :
		ALIMENTORECT[iteracion].top = ALIMENTORECT[iteracion].top *200
	VELOCIDADY[iteracion] = 3

while True:
	SCREEN.blit(FONDO,(0,0)) #Colocacion fondo
	pygame.draw.line(SCREEN,NEGRO,(0,0),(960,0),50) #Barra superior
	SCREEN.blit(textSurfaceObject,textRectObject) #Coloca texto puntos con puntuacion
	for iteracion in range(0,CANTIDADALIMENTOS+1):
		if ALIMENTORECT[iteracion]:
			SCREEN.blit(ALIMENTO,ALIMENTORECT[iteracion])
			ALIMENTORECT[iteracion].move_ip(ALIMENTOX,random.randrange(0,10))

	for event in pygame.event.get():
		if event.type == QUIT:		
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEMOTION: #Movimiento pez con mouse
			SCREEN.blit(PEZ,(event.pos))

	pygame.display.update()
	frecuencia.tick(FPS)


