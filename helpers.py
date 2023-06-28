import pygame
from constantes import *

def mandale_nave(numero):
    if(numero == 1):
        return NAVE_ENEMIGA_1
    if(numero == 2):
        return NAVE_ENEMIGA_2
    if(numero == 3):
        return NAVE_ENEMIGA_3

def mandale_boss(numero):
    if numero == 1:
        return NAVE_BOSS_1
    
    if numero == 2:
        return NAVE_BOSS_2
    

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
    max_x = maximo(lista)
    min_x = minimo(lista)
    if not max_x : return sentido
    if not min_x : return sentido

    if sentido == "DER":
        if max_x.rectangulo.x < ANCHO_VENTANA - TAMANIO_NAVE_ENEMIGA:
            for nave in lista:
                if nave.mostrar:
                    nave.rectangulo.x += nave.velocidad
        else:
            for nave in lista:
                if nave.mostrar:
                    nave.mover_abajo()
            sentido = "IZQ"

    elif sentido == "IZQ":
        if min_x.rectangulo.x > 0:
            for nave in lista:
                if nave.mostrar:
                    nave.rectangulo.x -= nave.velocidad
        else:
            for nave in lista:
                if nave.mostrar:
                    nave.mover_abajo()
            sentido = "DER"
    
    return sentido

def obtener_filas(nivel):
    if(nivel==1):
        return ENEMIGOS_FILA_LVL1
    if(nivel==2):
        return ENEMIGOS_FILA_LVL2
    if(nivel>=3):
        return ENEMIGOS_FILA_LVL3
def obtener_columnas(nivel):
    if(nivel == 1):
        return ENEMIGOS_COL_LVL1
    if(nivel == 2):
        return ENEMIGOS_COL_LVL2
    if(nivel == 3):
        return ENEMIGOS_COL_LVL3
    if(nivel == 4):
        return ENEMIGOS_COL_LVL4
    if(nivel >= 5):
        return ENEMIGOS_COL_LVL5

def maximo(lista):
    max_valor = lista[0]
    flag = False
    for valor in lista:
        if(valor.mostrar):
            flag = True
            if valor.rectangulo.x > max_valor.rectangulo.x:
                max_valor = valor
    if(not(flag)):
        max_valor = False
    return max_valor

def minimo(lista):
    min_valor = lista[0]
    flag = False
    for valor in lista:
        if(valor.mostrar):
            flag = True
            if valor.rectangulo.x < min_valor.rectangulo.x:
                min_valor = valor
    if not(flag):
        min_valor = False
    return min_valor

def bajar_naves(lista):
    for nave in lista:
        nave.rectangulo.y+=int(TAMANIO_NAVE_ENEMIGA/4)

def contar_enemigos_vivos(lista):
    lista_nueva = []
    for elem in lista:
        if elem.mostrar:
            lista_nueva.append(elem)
    return len(lista_nueva)
