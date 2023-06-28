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
        self.nombre = ""
        self.puntuacion=0
        self.boton1 = Button(master_surface=self.slave_surface,x=50,y=50,w=200,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.on_click_boton1, on_click_param="form_menu",text="VOLVER",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.boton2 = Button(master_surface=self.slave_surface,x=300,y=50,w=200,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.guardar, on_click_param="",text="CONFIRM",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonBorrar = Button(master_surface=self.slave_surface,x=550,y=50,w=200,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.borrar, on_click_param="",text="BORRAR",font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        
        self.botonA = Button(master_surface=self.slave_surface,x=50,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="A",text="A",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonB = Button(master_surface=self.slave_surface,x=100,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="B",text="B",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonC = Button(master_surface=self.slave_surface,x=150,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="C",text="C",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonD = Button(master_surface=self.slave_surface,x=200,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="D",text="D",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonE = Button(master_surface=self.slave_surface,x=250,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="E",text="E",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonF = Button(master_surface=self.slave_surface,x=300,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="F",text="F",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonG = Button(master_surface=self.slave_surface,x=350,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="G",text="G",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonH = Button(master_surface=self.slave_surface,x=400,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="H",text="H",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonI = Button(master_surface=self.slave_surface,x=400,y=150,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="I",text="I",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)

        self.botonJ = Button(master_surface=self.slave_surface,x=50,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="J",text="J",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonK = Button(master_surface=self.slave_surface,x=100,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="K",text="K",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonL = Button(master_surface=self.slave_surface,x=150,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="L",text="L",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonM = Button(master_surface=self.slave_surface,x=200,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="M",text="M",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonN = Button(master_surface=self.slave_surface,x=250,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="N",text="N",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonO = Button(master_surface=self.slave_surface,x=300,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="O",text="O",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonP = Button(master_surface=self.slave_surface,x=350,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="P",text="P",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonQ = Button(master_surface=self.slave_surface,x=400,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="Q",text="Q",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonR = Button(master_surface=self.slave_surface,x=400,y=200,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="R",text="R",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)

        self.botonS = Button(master_surface=self.slave_surface,x=50,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="S",text="S",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonT = Button(master_surface=self.slave_surface,x=100,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="T",text="T",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonU = Button(master_surface=self.slave_surface,x=150,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="U",text="U",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonV = Button(master_surface=self.slave_surface,x=200,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="V",text="V",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonW = Button(master_surface=self.slave_surface,x=250,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="W",text="W",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonX = Button(master_surface=self.slave_surface,x=300,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="X",text="X",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonY = Button(master_surface=self.slave_surface,x=350,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="Y",text="Y",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)
        self.botonZ = Button(master_surface=self.slave_surface,x=400,y=250,w=50,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click=self.set_nombre, on_click_param="Z",text="Z",font="arial",font_size=15,font_color=colores.COLOR_AMARILLO_MOSTAZA)

        self.botonNombre = Button(master_surface=self.slave_surface,x=100,y=500,w=500,h=50,color_back=colores.COLOR_AZUL, color_border=colores.COLOR_AMARILLO_MOSTAZA, on_click="", on_click_param="",text=self.nombre,font="arial",font_size=25,font_color=colores.COLOR_AMARILLO_MOSTAZA)
      
        

        self.lista_widget = [self.boton1,self.boton2,
                             self.botonA,self.botonB,self.botonC,self.botonD,self.botonE,self.botonF,self.botonG,self.botonH,self.botonI,
                             self.botonJ,self.botonK,self.botonL,self.botonM,self.botonN,self.botonO,self.botonP,self.botonQ,self.botonI,
                             self.botonR,self.botonS,self.botonT,self.botonU,self.botonV,self.botonW,self.botonX,self.botonY,self.botonI,
                             self.botonZ,self.botonNombre,self.botonBorrar]
    def set_nombre(self,param):
        print(param)
        print(self.nombre)
        self.nombre=self.nombre+param
        self.botonNombre.set_nombre(self.nombre)

    def borrar(self,param):
        print(param)
        self.nombre = ""
        self.botonNombre.set_nombre(self.nombre)

    def on_click_boton1(self,param):
        self.set_active("form_menu")
        print("entro en volver")
        
    def set_puntaje(self,param):

        self.puntuacion=param

    def guardar(self,param):
        data = []
        nuevo_registro = {
            "nombre": self.nombre,
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