import pygame, sys
from pygame.locals import *
import random
import os




pygame.init()
pygame.font.init()

FPS = 200
frecuencia = pygame.time.Clock()
SCREEN = pygame.display.set_mode((960,720),0,32)
pygame.display.set_caption('FishBowl v0.9')
random.randint(0, 960)

#Mouse
pygame.mouse.set_visible(False)
pygame.mouse.get_focused(True)
pygame.mouse.set_pos(430,360)

SCORE = 0
LEVEL = 1
LEVELMULT = 10

#Elementos graficos
AGUA = (72,177,230)
LETRAS = (240,247,25)
NEGRO = (0,0,0)
FONDO = pygame.image.load("back.jpg")

BURBUJA = pygame.image.load("bubble")
BURBUJARECT = BURBUJA.get_rect()

PEZ = pygame.image.load("fish")
PEZRECT = PEZ.get_rect()

COMIDA = pygame.image.load("food")											#cargando comida
COMIDARECT = COMIDA.get_rect()												#enmarcando comida

PEZD = pygame.image.load("fish_d")
ALIMENTO = pygame.image.load("food")
TEXTO = pygame.font.Font("Fishbowl.ttf",10)
TEXTO2 = pygame.font.Font("Fishbowl.ttf",50)
textSurfaceObject = TEXTO.render("PUNTOS: " + str(SCORE) +"      NIVEL: " + str(LEVEL),True,LETRAS,NEGRO)
textRectObject = textSurfaceObject.get_rect()
textSurfaceObject2 = TEXTO2.render("PERDISTE!",True,LETRAS,NEGRO)
textRectObject2 = textSurfaceObject.get_rect()
textRectObject2.center = (350,310)
textSurfaceObject3 = TEXTO.render("PRESIONA ESC PARA SALIR",True,LETRAS,NEGRO)
textRectObject3 = textSurfaceObject.get_rect()
textRectObject3.center = (430,400)

ycomida = 0																	#definiendo la x y a y de la comida
xcomida = random.randrange(1, 960,10)
yburbuja = 750
xburbuja = random.randrange(1,960,10)
#SCREEN.blit(COMIDA,(xcomida,ycomida))										#colocando la imagen sin marco en una posicion x y y
xpez,ypez = pygame.mouse.get_pos()
while True:
	#pos_mouse = pygame.mouse.get_pos()
    #mov_mouse = pygame.mouse.get_rel()

	SCREEN.blit(FONDO,(0,0)) #Colocacion fondo
	pygame.draw.line(SCREEN,NEGRO,(0,0),(960,0),50) #Barra superior
	textSurfaceObject = TEXTO.render("PUNTOS: " +str(SCORE) +"      NIVEL: " + str(LEVEL),True,LETRAS,NEGRO)
	COMIDARECT.left = xcomida 												#con esto se situa el marco de la comida
	COMIDARECT.top  = ycomida
	#SCREEN.blit(COMIDA,(xcomida,ycomida))									#colocando la imagen sin marco en una posicion x y y									
	SCREEN.blit(COMIDA,COMIDARECT)											#colocando la imagen con marco en una posicion
	PEZRECT.left = xpez														#colocando al rectangulo del pez en la coordenada x del mouse
	PEZRECT.top = ypez														#colocando al rectangulo del pez en la coordenada y del mouse
	SCREEN.blit(PEZ,PEZRECT)
	aumentovelocidad	= 2													#colocando al pez dentro del rectangulo
	BURBUJARECT.left = xburbuja
	BURBUJARECT.top = yburbuja
	SCREEN.blit(BURBUJA,BURBUJARECT)
	
	#****************************************************************
	#ESTA PARTE DE CODIGO MUEVE LA COMIDA
	if ycomida >= 700:
		xcomida = random.randrange(1, 960,10)
		ycomida = 0
		SCORE -= 1
		#SCREEN.blit(COMIDA,(xcomida,ycomida))
	elif ycomida < 700:
		aumentovelocidad += 6
		ycomida = ycomida + aumentovelocidad

	#****************************************************************
	#ESTA PARTE DE CODIGO MUEVE A LA BURBUJA
	if yburbuja <= 0:
		xburbuja = random.randrange(1,960,10)
		yburbuja = 750
	elif yburbuja >  0:
		yburbuja -= 8
		
		
	#*****************************************************************
	#ESTA PARTE DE CODIGO MUEVE AL PEZ Y VERIFICA SI SE QUIERE SALIR DE JUEGO

	for event in pygame.event.get():
		#SCREEN.blit(PEZRECT,pygame.mouse.get_pos())
		if event.type == QUIT:		
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEMOTION: #Movimiento pez con mouse
		 	xpez,ypez = pygame.mouse.get_pos()
	#**********************************************************************
			
	if PEZRECT.colliderect(COMIDARECT):
		SCORE += 1
		xcomida = random.randrange(1, 960,10)
		ycomida = 0
		if SCORE == LEVELMULT:
			LEVEL = LEVEL+1
			LEVELMULT = LEVELMULT*LEVEL
	elif SCORE < 0:
		SCREEN.blit(textSurfaceObject2,textRectObject2)
		SCREEN.blit(textSurfaceObject3,textRectObject3)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()
	SCREEN.blit(textSurfaceObject,textRectObject)
	pygame.display.update()
	frecuencia.tick(FPS)

