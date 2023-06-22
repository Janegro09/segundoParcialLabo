import pygame
from constantes import *

def mandale_nave(numero):
    if(numero == 1):
        return NAVE_ENEMIGA_1
    if(numero == 2):
        return NAVE_ENEMIGA_2
    if(numero == 3):
        return NAVE_ENEMIGA_3

def get_superficie_sprite(path, filas, columnas ):
    lista = []
    surface_image = pygame.image.load(path)
    fotograma_ancho = int(surface_image.get_width()/filas)
    fotograma_alto = int(surface_image.get_height()/columnas)
    for j in range(columnas):
        for i in range(filas):
            x = i*fotograma_ancho
            y = j*fotograma_alto
            surface_fotograma = surface_image.subsurface(x,y,fotograma_ancho,fotograma_alto)     
            lista.append(surface_fotograma)
    return lista

def escalar(lista, tam = TAM):
    nueva_lista = []
    for img in lista:
        nueva_img = pygame.transform.scale(img,tam)
        nueva_lista.append(nueva_img)
    return nueva_lista


def mover_naves(lista, sentido):
    #DERECHA
    if(sentido == "DER"):
        for nave in lista:
            if nave.rectangulo.x + TAMANIO_NAVE_ENEMIGA < ANCHO_VENTANA:
                if(nave.mostrar):
                    nave.rectangulo.x+=nave.velocidad
            else:
                bajar_naves(lista)
                sentido = "IZQ"
    #IZQUIERDA
    if(sentido == "IZQ"):
        for nave in lista:
            if nave.rectangulo.x > 0:
                if(nave.mostrar):
                    nave.rectangulo.x-=nave.velocidad
            else:
                bajar_naves(lista)
                sentido = "DER"

    return sentido

def bajar_naves(lista):
    for nave in lista:
        nave.rectangulo.y+=int(TAMANIO_NAVE_ENEMIGA/4)

def contar_enemigos_vivos(lista):
    lista_nueva = []
    for elem in lista:
        if elem.mostrar:
            lista_nueva.append(elem)
    return len(lista_nueva)
