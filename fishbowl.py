import pygame, sys
from pygame.locals import *
import random
pygame.init()
pygame.font.init()

FPS = 30
frecuencia = pygame.time.Clock()
SCREEN = pygame.display.set_mode((960,720),0,32)
pygame.display.set_caption('FishBowl v0.3')
random.randint(0, 960)

#Mouse
pygame.mouse.set_visible(False)
pygame.mouse.get_focused(True)
pygame.mouse.set_pos(430,360)

SCORE = 0

#Elementos graficos
AGUA = (72,177,230)
LETRAS = (240,247,25)
NEGRO = (0,0,0)
FONDO = pygame.image.load("back.jpg")
PEZ = pygame.image.load("fish")
PEZD = pygame.image.load("fish_d")
ALIMENTO = pygame.image.load("food")
TEXTO = pygame.font.Font("Fishbowl.ttf",10)
textSurfaceObject = TEXTO.render("PUNTOS: " + str(SCORE),True,LETRAS,NEGRO)
textRectObject = textSurfaceObject.get_rect()

while True:
	SCREEN.blit(FONDO,(0,0)) #Colocacion fondo
	pygame.draw.line(SCREEN,NEGRO,(0,0),(960,0),50) #Barra superior
	SCREEN.blit(textSurfaceObject,textRectObject)
	for event in pygame.event.get():
		if event.type == QUIT:		
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEMOTION: #Movimiento pez con mouse
			SCREEN.blit(PEZ,(event.pos))


	pygame.display.update()
	frecuencia.tick(FPS)


