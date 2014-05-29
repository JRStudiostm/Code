#Chelin Tutorials. Todos los Derechos Reservados.
#sitio web: http://chelintutorials.blogspot.com/


import pygame
import random


class Recs(object):
    def __init__(self,numeroinicial):
        self.lista=[]
        for x in range(numeroinicial):
            #creo un rect random
            leftrandom=random.randrange(2,560)
            toprandom=random.randrange(-580,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista.append(pygame.Rect(leftrandom,toprandom,width,height))            
    def reagrear(self):
        for x in range(len(self.lista)):
            if self.lista[x].top>482:
                leftrandom=random.randrange(2,560)
                toprandom=random.randrange(-580,-10)
                width=random.randrange(10,30)
                height=random.randrange(15,30)
                self.lista[x]=(pygame.Rect(leftrandom,toprandom,width,height)) 

    def agregarotro(self):
        pass
    def mover(self):
        for rectangulo in self.lista:
            rectangulo.move_ip(0,2)
    def pintar(self,superficie):
        for rectangulo in self.lista:
            pygame.draw.rect(superficie,(200,0,0),rectangulo)

class Circ(object):
    def __init__(self,numeroinicial):
        self.lista1=[]
        for x in range(numeroinicial):
            #creo un circulo random  
            leftrandom=random.randrange(2,560)          #cambiar a dimenciones que necesita un circulo..
            toprandom=random.randrange(-580,-10)
            width=random.randrange(10,30)
            height=random.randrange(15,30)
            self.lista1.append(pygame.Circ(leftrandom,toprandom,width,height))            
    def reagrear(self):
        for x in range(len(self.lista)):
            if self.lista1[x].top>482:
                leftrandom=random.randrange(2,560)
                toprandom=random.randrange(-580,-10)
                width=random.randrange(10,30)
                height=random.randrange(15,30)
                self.lista1[x]=(pygame.Circ(leftrandom,toprandom,width,height)) 

    def agregarotro(self):
        pass
    def mover(self):
        for circulo in self.lista1:
            circulo.move_ip(0,2)
    def pintar(self,superficie):
        for circulo in self.lista1:
            pygame.draw.circle(superficie,(0,0,255),circulo)  #Investigar que valores recive uun circulo
            
class Player(pygame.sprite.Sprite):
    def __init__(self,imagen):
        self.imagen=imagen

        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
        if self.rect.left<0:
            vx=-vx
        self.rect.move_ip(vx,vy)

    def update(self,superficie):
        superficie.blit(self.imagen,self.rect)

def colision(player,recs):
    for rec in recs.lista:
        if player.rect.colliderect(rec):
            return True
    return False

def comer(player, recs):
    for rec in recs.lista:
        if plater.rect.colliderect(rec)
            

def main():
    import pygame
    
    pygame.init()
    pantalla=pygame.display.set_mode((600,480))
    salir=False
    reloj1= pygame.time.Clock()
    imagen1=pygame.image.load("pez1.png").convert_alpha()
    imagenexplosion=pygame.image.load("morido.png").convert_alpha()
    imagenfondo=pygame.image.load("111.jpg").convert_alpha()
    pygame.mixer.music.load("play.mid")
    sonido1=pygame.mixer.Sound("1.mid")
    recs1=Recs(25)
    circ1=Circ(30)
    player1=Player(imagen1)
    
    #variables aux
    player1=Player(imagen1)
    vx,vy=0,0
    velocidad=10
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    colisiono=False
    
    pygame.mixer.music.play(2)
    while salir!=True:#LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if colisiono==False:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-velocidad
                        sonido1.play()
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=velocidad
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-velocidad
                        else:vy=0                    
        
        reloj1.tick(20)
        

        if colision(player1,recs1):
            colisiono=True
            player1.imagen=imagenexplosion
            pygame.mixer.music.stop()
        if colisiono==False:    
            recs1.mover()
            player1.mover(vx, vy)     
               
        pantalla.blit(imagenfondo,(0,0))
        circ1.pintar(pantalla)
        recs1.pintar(pantalla)
        player1.update(pantalla)
        pygame.display.update()
        circ1.reagrear()
        recs1.reagrear()        
    pygame.quit()

main()