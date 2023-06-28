import pygame
import colores
from gui_form import Form
from gui_buttom import Button

class FormMenuA(Form):
    def __init__(self,name, master_surface, x, y, w, h, color_back, color_border, active):
        super().__init__(name,master_surface, x, y, w, h, color_back, color_border, active)

        self.boton1 = Button(master_surface=self.slave_surface,x=100,y=50,w=150,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.on_click_boton1, on_click_param="Comenzamos el juego",text="START",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.boton2 = Button(master_surface=self.slave_surface,x=100,y=150,w=150,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.ir_a, on_click_param="form_menu2",text="SCORE",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self,param):
        print("Hola",param)


    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_boton in self.lista_widget:
            aux_boton.draw()
