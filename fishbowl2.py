import pygame, sys
from pygame.locals import *
import random
import os
import commands




pygame.init()
pygame.font.init()

FPS = 200
frecuencia = pygame.time.Clock()
SCREEN = pygame.display.set_mode((960,720),0,32)
pygame.display.set_caption('FishBowl v0.9.4')
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
PEZ2 = pygame.image.load("fish2")
PEZD = pygame.image.load("fish_d")
PEZRECT = PEZ.get_rect()
PEZ2RECT = PEZ2.get_rect()

COMIDA = pygame.image.load("food")											#cargando comida
COMIDARECT = COMIDA.get_rect()												#enmarcando comida

LEVELUP = pygame.image.load("verde")
LEVELUPRECT = LEVELUP.get_rect()

SCOREDOWN = pygame.image.load("rojo")
SCOREDOWNRECT = LEVELUP.get_rect()

BUG = pygame.image.load("bug")
BUGRECT = BUG.get_rect()

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
textSurfaceObject4 = TEXTO2.render("Level UP!",True,LETRAS,NEGRO)
textRectObject4 = textSurfaceObject.get_rect()
textRectObject4.center = (350,310)

ycomida = 0																	#definiendo la x y a y de la comida
xcomida = random.randrange(1, 960,10)
yburbuja = 750
xburbuja = random.randrange(1,960,10)
#SCREEN.blit(COMIDA,(xcomida,ycomida))										#colocando la imagen sin marco en una posicion x y y
ybug = -200 			# LE PUSE ESTE VALOR PARA QUE HAYA UN RETRASO DE TIEMPO PARA QUE APAREZCA EN LA PANTALLA
xbug = random.randrange(1,960,10)
xpez,ypez = pygame.mouse.get_pos()
pygame.mixer.music.load("loop.wav")
pygame.mixer.music.play(-1,0)

while True:
	#pos_mouse = pygame.mouse.get_pos()
    #mov_mouse = pygame.mouse.get_rel()

	SCREEN.blit(FONDO,(0,0)) #Colocacion fondo
	pygame.draw.line(SCREEN,NEGRO,(0,0),(960,0),50) #Barra superior
	textSurfaceObject = TEXTO.render("PUNTOS: " +str(SCORE) +"      NIVEL: " + str(LEVEL),True,LETRAS,NEGRO)
	COMIDARECT.left = xcomida 												#con esto se situa el marco de la comida
	COMIDARECT.top  = ycomida
	#SCREEN.blit(COMIDA,(xcomida,ycomida))									#colocando la imagen sin marco en una posicion x y y									
	BURBUJARECT.left = xburbuja
	BURBUJARECT.top = yburbuja
	BUGRECT.left = xbug
	BUGRECT.top  = ybug
	SCREEN.blit(BUG,BUGRECT)
	SCREEN.blit(COMIDA,COMIDARECT)											#colocando la imagen con marco en una posicion
	SCREEN.blit(BURBUJA,BURBUJARECT)
	aumentovelocidad	= 2													#colocando al pez dentro del rectangulo
	velocidadbicho = 2
	
	
	if ypez<xpez:
		PEZ2RECT.left = xpez														#colocando al rectangulo del pez en la coordenada x del mouse, dependiendo del como este orientado es si muestra al pez a la derecha o izquierda
		PEZ2RECT.top = ypez
		SCREEN.blit(PEZ2,PEZ2RECT)
	if xpez<ypez:
		PEZRECT.left = xpez														#colocando al rectangulo del pez en la coordenada x del mouse
		PEZRECT.top = ypez
		SCREEN.blit(PEZ,PEZRECT)												#colocando al rectangulo del pez en la coordenada y del mouse
	aumentovelocidad	= 2													#colocando al pez dentro del rectangulo
	BURBUJARECT.left = xburbuja
	BURBUJARECT.top = yburbuja
	SCREEN.blit(BURBUJA,BURBUJARECT)

	#****************************************************************
	#ESTA PARTE DE CODIGO MUEVE LA COMIDA
	if ycomida >= 700:
		xcomida = random.randrange(1, 960,10)
		ycomida = 0
		SCORE -= LEVEL*2
		SCREEN.blit(SCOREDOWN,SCOREDOWNRECT)
		#SCREEN.blit(COMIDA,(xcomida,ycomida))
	elif ycomida < 700:
		aumentovelocidad += 3
		ycomida = ycomida + aumentovelocidad*LEVEL

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
			pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEMOTION: #Movimiento pez con mouse
		 	xpez,ypez = pygame.mouse.get_pos()
	#**********************************************************************
		#ESTA PARTE DE CODIGO MUEVE A EL BICHEJO =)
		if ybug >= 700:
			xbug = random.randrange(1,960,10)
			ybug = 0
		elif ybug < 700:
			velocidadbicho *= 3
			ybug = ybug + velocidadbicho*LEVEL
	#***********************************************************************

	if PEZRECT.colliderect(COMIDARECT) or PEZ2RECT.colliderect(COMIDARECT):
		SCORE += 1
		xcomida = random.randrange(1, 960,10)
		ycomida = 0
		if SCORE == LEVELMULT:
			LEVEL = LEVEL+1
			LEVELMULT = LEVELMULT*LEVEL
			SCREEN.blit(LEVELUP,LEVELUPRECT)
	elif PEZRECT.colliderect(BUGRECT) or PEZ2RECT.colliderect(BUGRECT):
			SCORE -= 1
			xbug = random.randrange(1,960,10)
			ybug = -200
	elif SCORE < 0:
		SCREEN.blit(textSurfaceObject2,textRectObject2)
		SCREEN.blit(textSurfaceObject3,textRectObject3)
		SCREEN.blit(PEZD,(380,50))
		xpez = -138
		ypez = -91
		ycomida = 0
		aumentovelocidad = 0
		velocidadbicho =0
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.mouse.set_visible(True)
				os.system('python compilado.py')
				sys.exit()
	SCREEN.blit(textSurfaceObject,textRectObject)
	pygame.display.update()
	frecuencia.tick(FPS)
