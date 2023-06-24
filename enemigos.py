import pygame
import colores
import random
from constantes import *
from helpers import *
from disparos import Disparar

class Enemigos:
    def __init__(self,posx,posy,puntaje,nivel,parametro,tipo="Minion",cantVidas=1) -> None:

        self.superficie = get_superficie_sprite(PATH_IMG+parametro,1,1)
        self.vidas = cantVidas
        self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
        self.tipo = tipo
        self.nivel = nivel
        if(tipo=="Boss"):
            self.superficie = escalar(self.superficie,(TAMANIO_BOSS_ENEMIGA,TAMANIO_BOSS_ENEMIGA))
            posy = -TAMANIO_BOSS_ENEMIGA
            self.primera_pasada = True
            self.velocidad = 3
            self.muere = escalar(self.muere,(TAMANIO_BOSS_ENEMIGA,TAMANIO_BOSS_ENEMIGA))
            self.frecuencia = random.randint(2500,10000)
            self.velocidad_disparo = 1.25*self.nivel
        else:
            self.superficie = escalar(self.superficie,(TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA))
            self.velocidad = 5
            self.muere = escalar(self.muere)
            self.frecuencia = random.randint(2500,20000)

        self.frame = 0
        self.animacion = self.superficie
        self.imagen = self.animacion[self.frame]
        self.animacion_repetir = True
        self.disparos = []
        self.limite_disparos = random.randint(1,10)
        self.disparo = False
        self.velocidad_disparo = 1*self.nivel
        self.sentido_derecho =True
        self.sentido_izquierdo = False
        self.tiempo = 0
        self.tiempo_boss = 0
        self.tiempo_disparo = 0

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.centerx = posx
        self.rectangulo.y = posy
        
        self.mostrar = True
        self.puntaje = puntaje

    def disparar(self,potenciador):
        if(self.tipo =="Minion"):
            if self.tiempo > self.frecuencia:
                self.tiempo = 0
                if (self.limite_disparos > len(self.disparos) and self.mostrar) :
                    disparo = Disparar(self.rectangulo.centerx, self.rectangulo.y,"Minion")
                    self.disparo = True
                    self.disparos.append(disparo)
        if(self.tipo == "Boss"):
            if self.tiempo > self.frecuencia:
                if (self.limite_disparos > len(self.disparos) and self.mostrar) :
                    disparo = Disparar(self.rectangulo.centerx, self.rectangulo.y,"Boss")
                    self.disparo = True
                    self.disparos.append(disparo)

    def mover_derecha(self):
        self.rectangulo.x +=self.velocidad

    def mover_izquierda(self):
        self.rectangulo.x -=self.velocidad
    
    def intro_boss(self, tiempo_ms):
        if self.primera_pasada:
            self.rectangulo.y+=10
            if(self.rectangulo.y > ALTO_VENTANA):
                self.primera_pasada=False
                self.rectangulo.y=-ANCHO_VENTANA
        else:
            if(self.rectangulo.y < 0):
                self.rectangulo.y+=5
            else:
                mover = random.randint(1,2)

                if mover == 1 and self.sentido_derecho:
                    self.tiempo_boss+=tiempo_ms
                    if(self.rectangulo.x < ANCHO_VENTANA-TAMANIO_BOSS_ENEMIGA):
                        self.mover_derecha()
                    if(self.tiempo_boss > 750):
                        self.tiempo_boss=0
                        self.sentido_derecho = False
                        self.sentido_izquierdo = True

                if mover == 2 and self.sentido_izquierdo:
                    self.tiempo_boss+=tiempo_ms
                    if(self.rectangulo.x > 0):
                        self.mover_izquierda()
                    if(self.tiempo_boss > 750):
                        self.tiempo_boss=0
                        self.sentido_derecho = True
                        self.sentido_izquierdo = False
                        self.mover_izquierda()
        
    def mover(self, direccion):
        if(direccion):
            self.mover_derecha()
        else:
            self.mover_izquierda()

    def update(self,delta_ms,potenciador,disparos=[]):

        self.tiempo+=delta_ms
        self.disparar(potenciador)
        #Recargamos, es decir si el misil salió de la pantalla lo eliminamos del listado
        if(len(self.disparos) > 0):
            if(self.disparos[0].rectangulo.y > ANCHO_VENTANA):
                self.disparos.pop(0)    

        for misil in disparos:
            if self.rectangulo.colliderect(misil.rectangulo):
                if(self.animacion != self.muere):
                    self.animacion = self.muere
                    misil.mostrar = False
        if(self.animacion == self.muere):
            if(self.frame < len(self.animacion)-1):
                self.frame +=1
            else:
                self.mostrar = False

        self.imagen = self.animacion[self.frame]

    def draw(self,pantalla):
        if(self.mostrar):
            pantalla.blit(self.imagen, self.rectangulo)

    @property
    def posicion(self):
        return self.rectangulo.x
