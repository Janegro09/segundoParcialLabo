import pygame
import colores
from gui_form import Form
from gui_buttom import Button
import re
import json
from constantes import *

class FormMenuB(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_back, color_border, active):
        super().__init__(name,master_surface, x, y, w, h, color_back, color_border, active)

        self.boton1 = Button(master_surface=self.slave_surface,x=ANCHO_VENTANA-200,y=50,w=150,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.ir_a, on_click_param="form_menu",text="VOLVER",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.lista_widget = [self.boton1]

    def on_click_boton1(self,param):
        print("Hola",param)

    def update(self, lista_eventos):

        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def mostrar_top(self):
        posx=100
        posy=100
        total=0
        lista = []
        with open('score.json') as file:
            data = json.load(file)
            for info in data:
                nombre = "{} - {}".format(info['nombre'],info['puntaje'])
                total+=1
                lista.append(Button(master_surface=self.slave_surface,x=posx,y=posy*total,w=200,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click="", on_click_param="",text=nombre,font="arial",font_size=20,font_color=colores.COLOR_AMARILLO_MOSTAZA))


        for aux in lista:
            aux.draw()


    def draw(self):
        super().draw()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
        self.mostrar_top()