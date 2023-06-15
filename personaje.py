import pygame
import colores

def crear(x,y,ancho, alto, path):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load(path)
    dict_personaje["surface"] =  pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    
    dict_personaje["rect"] = dict_personaje["surface"].get_rect()
    dict_personaje["rect"].centerx = x
    dict_personaje["rect"].y = y
    
    rect_nave = pygame.Rect(250,400,40,40)

    return dict_personaje

def actualizar_pantalla(personaje, pantalla):
    pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, personaje["rect"])
    pantalla.blit(personaje["surface"],personaje["rect"])

def mover(nave,ancho,alto):
    ancho_nave = nave["rect"].width
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_RIGHT] and nave["rect"].x < ancho - ancho_nave:
        nave["rect"].x = nave["rect"].x + 1
    if lista_teclas[pygame.K_LEFT] and nave["rect"].x > 0:
        nave["rect"].x = nave["rect"].x - 1
    # if lista_teclas[pygame.K_UP] and nave[1] > 0:
    #     nave[1] = nave[1] - 5
    # if lista_teclas[pygame.K_DOWN] and nave[1] < alto - ancho_nave:
    #     nave[1] = nave[1] + 5