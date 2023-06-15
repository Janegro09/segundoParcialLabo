import pygame
import colores

def crear(x,y,ancho, alto):
    dict_personaje = {}
    dict_personaje["surface"] = pygame.image.load("galaxia\img\ship.png")
    dict_personaje["surface"] =  pygame.transform.scale(dict_personaje["surface"],(ancho,alto))
    
    dict_personaje["rect"] = dict_personaje["surface"].get_rect()
    dict_personaje["rect"].centerx = x
    dict_personaje["rect"].y = y
    
    rect_nave = pygame.Rect(250,400,40,40)

    return dict_personaje

def actualizar_pantalla(personaje, pantalla):
    pygame.draw.rect(pantalla, colores.COLOR_ROJO_INDIAN, personaje["rect"])
    pantalla.blit(personaje["surface"],personaje["rect"])

