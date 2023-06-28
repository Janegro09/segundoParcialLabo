import pygame
from gui_buttom import Button

class Form():
    form_dic = {}
    def __init__(self,name,master_surface,x,y,w,h,color_back, color_border, active):
        self.form_dic[name]=self
        self.master_surface = master_surface
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.color_back = color_back
        self.color_border = color_border

        self.slave_surface = pygame.Surface((w,h))
        
        self.slave_rect = self.slave_surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        if(self.color_back != None):
            self.slave_surface.fill(self.color_back)

    def set_active(self,name):
        for aux_form in self.form_dic.values():
            aux_form.active = False
        self.form_dic[name].active = True
    
    def set_unactive(self,name):
        # for aux_form in self.form_dic.values():
        #     aux_form.active = False
        self.form_dic[name].active = False
    
    def ir_a(self, param):
        self.set_active(param)

    def render(self):
        pass

    def update(self, lista_eventos):
        pass        

    def draw(self):
        self.master_surface.blit(self.slave_surface,self.slave_rect)
