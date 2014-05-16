import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 30
frecuencia = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Protipo Proyecto')
SKY = (112,118,144)
CLOUD = (192,192,192)
SUN = (255,255,255)
RED = (255,0,0)
GUY = pygame.image.load("personaje.png")
FOREST = pygame.image.load("arbusto.png")
FINISH = pygame.image.load("meta.png")
GUYX = 20
GUYY = 460
FORESTX = -100
FORESTY = 450
FINISHX = 620
FINISHY = 470
CLOUD1_DIM = [100,500,200,100]
CLOUD2_DIM = [300,100,200,100]
aumX = 0
aumY = 0
fontObject = pygame.font.Font("StripeAttack.ttf",40)
textSurfaceObject = fontObject.render("Titulo del estupido Juego",True,RED,SKY)
textRectObject = textSurfaceObject.get_rect()
textRectObject.center = (200,30)
fontObject2 = pygame.font.Font("StripeAttack.ttf",60)
textSurfaceObject2 = fontObject2.render("Ganaste",True,RED,SKY)
textRectObject2 = textSurfaceObject.get_rect()
textRectObject2.center = (400,300)
#pygame.mixer.music.load("Molinos_de_viento.mp3")
#pygame.mixer.music.play(-1,0,0)
while True:
	SCREEN.fill(SKY)
	pygame.draw.circle(SCREEN,SUN,(700,100),120,0)
	pygame.draw.ellipse(SCREEN,CLOUD,CLOUD1_DIM,0)
	pygame.draw.ellipse(SCREEN,CLOUD,CLOUD2_DIM,0)
	SCREEN.blit(FOREST,(FORESTX,FORESTY))
	SCREEN.blit(FOREST,(FORESTX+200,FORESTY))
	SCREEN.blit(FOREST,(FORESTX+340,FORESTY))
	SCREEN.blit(FOREST,(FORESTX+500,FORESTY))
	SCREEN.blit(FOREST,(FORESTX+660,FORESTY))
	SCREEN.blit(FINISH,(FINISHX,FINISHY))
	SCREEN.blit(GUY,(GUYX,GUYY))
	SCREEN.blit(textSurfaceObject,textRectObject)
	GUYX = GUYX + aumX
	GUYY = GUYY + aumY
	if GUYX >= 800:
		SCREEN.blit(textSurfaceObject2,textRectObject2)
	for event in pygame.event.get():
		if event.type == QUIT:
			#pygame.mixer.music.stop()
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				aumX = 5
			if event.key == pygame.K_LEFT:
				aumX = -5
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				aumX = 0
			if event.key == pygame.K_LEFT:
				aumX = 0
	pygame.display.update()
	frecuencia.tick(FPS)