import pygame
import colores
import random
from constantes import *
from helpers import *
from disparos import Disparar

class Enemigos:
    def __init__(self,posx,posy,puntaje,nivel,parametro) -> None:

        self.superficie = get_superficie_sprite(PATH_IMG+parametro,1,1)
        self.superficie = escalar(self.superficie,(TAMANIO_NAVE_ENEMIGA,TAMANIO_NAVE_ENEMIGA))
        self.muere = get_superficie_sprite(PATH_IMG+"explosion.png",3,2)
        self.muere = escalar(self.muere)
        self.frame = 0
        self.nivel = nivel
        self.animacion = self.superficie
        self.imagen = self.animacion[self.frame]
        self.animacion_repetir = True
        self.limite_disparos = 10
        self.disparos = []
        self.frecuencia = random.randint(1,DIFICULTAD/nivel)
        self.disparo = False
        self.velocidad_disparo = 1*self.nivel
        self.velocidad = 5
        self.sentido_derecho =True
        self.sentido_izquierdo = False
        self.tiempo = 0

        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posx
        self.rectangulo.y = posy
        
        self.mostrar = True
        self.puntaje = puntaje

    def disparar(self,potenciador):
        if self.tiempo % int(self.frecuencia/potenciador) == 0:
            if (self.limite_disparos > len(self.disparos) and self.mostrar) :
                disparo = Disparar(self.rectangulo.centerx, self.rectangulo.y,"enemigo")
                self.disparo = True
                self.disparos.append(disparo)

    def mover_derecha(self):
        self.rectangulo.x +=self.velocidad

    def mover_izquierda(self):
        self.rectangulo.x -=self.velocidad

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
