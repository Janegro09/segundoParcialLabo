# from enemigos import NaveVerde
import pygame

def get_superficie_sprite(path, filas, columnas ):
    lista = []
    surface_image = pygame.image.load(path)
    fotograma_ancho = int(surface_image.get_width()/filas)
    fotograma_alto = int(surface_image.get_height()/columnas)
    for j in range(columnas):
        for i in range(filas):
            x = i*fotograma_ancho
            y = j*fotograma_alto
            print(x,y,fotograma_ancho,fotograma_alto)
            surface_fotograma = surface_image.subsurface(x,y,fotograma_ancho,fotograma_alto)     
            lista.append(surface_fotograma)
    return lista

def mover_naves(lista,ancho, tamanio_nave,sentido):
    primera = lista[0]
    ultima = lista[len(lista) -1]
    
    #si es de izquierda o derecha
    if(primera.posicion < 0):
        sentido = not(sentido)
    else:
        if(ultima.posicion > ancho-tamanio_nave):
            sentido = not(sentido)

    for nave in lista: 
        nave.mover(sentido)
    return sentido