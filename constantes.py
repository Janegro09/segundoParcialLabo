import pygame

ALTO_VENTANA = 600
ANCHO_VENTANA = 720
FPS = 10

#IMAGENES
PATH_IMG = "img/"

#ENEMIGOS
BASE_ENEMIGA = 10
TAMANIO_NAVE_ENEMIGA = 60
DESPLAZAMIENTO = 5

#PLAYER
VELOCIDAD_NAVE_PPAL=5
VIDAS = 3
imagen_player = pygame.image.load(PATH_IMG+"player_ship.png")
TAM = (int(imagen_player.get_width()/4),imagen_player.get_height())