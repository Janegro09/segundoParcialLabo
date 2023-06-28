import pygame
import colores
from gui_form import Form
from gui_buttom import Button
import re
import json
import operator

class FormMenuC(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_back, color_border, active):
        super().__init__(name,master_surface, x, y, w, h, color_back, color_border, active)

        self.boton1 = Button(master_surface=self.slave_surface,x=100,y=50,w=150,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.on_click_boton1, on_click_param="form_menu",text="VOLVER",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.boton2 = Button(master_surface=self.slave_surface,x=300,y=50,w=150,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.guardar, on_click_param="",text="CONFIRMAR",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self,param):
        self.set_active(param)
        
    def set_puntaje(self,param):

        self.puntuacion=str(param)

    def guardar(self,param):
        data = []
        nuevo_registro = {
            "nombre": "Javo",
            "puntaje": self.puntuacion
        }

        with open('score.json', 'r') as file:
            data = json.load(file)

        data.append(nuevo_registro)
        print(data)
        # Ordenar los registros por puntaje de mayor a menor

        n = len(data)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if int(data[j]['puntaje']) < int(data[j + 1]['puntaje']):
                    data[j], data[j + 1] = data[j + 1], data[j]

        data.pop()
        # Volver a escribir el archivo JSON con los datos ordenados
        with open('score.json', 'w') as file:
            json.dump(data, file)

        self.set_active("form_menu")

    def update(self, lista_eventos):

        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
        # self.mostrar_top()