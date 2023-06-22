import pygame

ALTO_VENTANA = 600
ANCHO_VENTANA = 720
FPS = 60

#IMAGENES
PATH_IMG = "img/"
PATH_MSC = "music/"

#ENEMIGOS
BASE_ENEMIGA = 10
TAMANIO_NAVE_ENEMIGA = 60
DESPLAZAMIENTO = 5
DIFICULTAD = 10000
NAVE_ENEMIGA_1 = "spiked1.png"
NAVE_ENEMIGA_2 = "spiked2.png"
NAVE_ENEMIGA_3 = "spiked3.png"
#PLAYER
VELOCIDAD_NAVE_PPAL=5
VIDAS = 3
imagen_player = pygame.image.load(PATH_IMG+"player_ship.png")
TAM = (int(imagen_player.get_width()/4),imagen_player.get_height())