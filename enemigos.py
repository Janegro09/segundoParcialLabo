import pygame
import colores

def crear_enemigo(x,y,ancho,alto,parametro):
    imagen_nave = pygame.image.load(parametro)
    imagen_nave = pygame.transform.scale(imagen_nave,(ancho,alto))

    rect_nave = imagen_nave.get_rect()
    rect_nave.x = x
    rect_nave.y = y

    dict_enemigo = {}
    dict_enemigo["surface"] = imagen_nave
    dict_enemigo["rect"] = rect_nave

    return dict_enemigo

def update_left(lista_enemigos, ancho, tam, cambiar_sentido):
    print("entro a left")
    primera_nave = lista_enemigos[0]
    #muevo a la izquierda
    if(primera_nave["rect"][0] > 0  ):
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[0] = rect_enemigo[0] - 10
    #bajo todo
    else:
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[1] = rect_enemigo[1] + tam
        cambiar_sentido = not(cambiar_sentido)
        print(primera_nave["rect"][0])

    return cambiar_sentido

def update_right(lista_enemigos, ancho, tam, cambiar_sentido):
    print("Entro a right")
    ultima_nave = lista_enemigos[len(lista_enemigos) - 1]
    #muevo a la izquierda
    ancho_nave = ultima_nave["rect"].width
    if(ultima_nave["rect"][0] < ancho - ancho_nave ):
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[0] = rect_enemigo[0] + 10
    #bajo todo
    else:
        for enemigo in lista_enemigos:
            rect_enemigo = enemigo["rect"]
            rect_enemigo[1] = rect_enemigo[1] + tam
        cambiar_sentido = not(cambiar_sentido)
        print(ultima_nave["rect"][0])

    return cambiar_sentido


def actualizar_pantalla(lista_enemigos, pantalla):
    for enemigo in lista_enemigos:
        pygame.draw.rect(pantalla, colores.COLOR_MARRON_AVENA, enemigo["rect"])
        pantalla.blit(enemigo["surface"],enemigo["rect"])

def crear_lista_enemigos(cant, x, y, ancho, alto, path_imagen):
    lista_naves = []
    pos_naves = 0
    for i in range(cant):
        lista_naves.append(crear_enemigo(x+pos_naves,y,ancho, alto, path_imagen))
        pos_naves=ancho + pos_naves +10
    return lista_naves