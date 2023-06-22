import pygame
import colores
import random
from constantes import *
from helpers import *
from disparos import Disparar

class NaveVerde:
    def __init__(self,posx,posy,puntaje,parametro) -> None:

        self.superficie = get_superficie_sprite(PATH_IMG+parametro,1,1)
        self.superficie = escalar(self.superficie,(TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA))
        self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
        self.muere = escalar(self.muere)
        self.frame = 0
        self.animacion = self.superficie
        self.imagen = self.animacion[self.frame]
        self.animacion_repetir = True
        self.limite_disparos = 10
        self.misiles = []
        self.frecuencia = random.randint(1,10000)
        self.disparo = False
        self.velocidad_disparo = 1
        self.velocidad = 5
        self.sentido_derecho =True
        self.sentido_izquierdo = False

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posx
        self.rectangulo.y = posy
        
        self.mostrar = True
        self.puntaje = puntaje

    def disparar(self):
        if (self.frecuencia % random.randint(1,DIFICULTAD) == 0 and self.limite_disparos > len(self.misiles) and self.mostrar) :
            disparo = Disparar(self.rectangulo.x, self.rectangulo.y,"enemigo")
            self.disparo = True
            self.misiles.append(disparo)

    def mover_derecha(self):
        self.rectangulo.x +=self.velocidad

    def mover_izquierda(self):
        self.rectangulo.x -=self.velocidad

    def mover(self, direccion):
        if(direccion):
            self.mover_derecha()
        else:
            self.mover_izquierda()

    def update(self, disparos=[]):

        self.disparar()

        for misil in disparos:
            if self.rectangulo.colliderect(misil.rectangulo):
                if(self.animacion != self.muere):
                    self.animacion = self.muere
                    misil.choco = True
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
