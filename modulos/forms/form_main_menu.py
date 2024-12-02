import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA

class FormMainMenu(Form):

    def __init__(self, name: str, pantalla, x: int, y: int, active: bool, level_num: int, music_path: str):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        self.start_first_level = False

        self.music_update()
        
        self.surface = pg.image.load("assets/img/forms/fondo-menu.png").convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.menu_ppal_title = TextTitle(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]-1000, texto= "THIS or THAT", pantalla=pantalla, font_size=150)
        self.menu_ppal_subtitle = TextTitle(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]-800, texto= "MENU PRINCIPAL", pantalla=pantalla, font_size=100)

        self.button_start = Button(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]//2+40, texto= "COMENZAR", pantalla=pantalla,font_size=50, on_click=self.click_start, on_click_param="form_enter_name")
        self.button_options = Button(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]//2+140, texto= "OPCIONES", pantalla=pantalla,font_size=50, on_click=self.click_option, on_click_param="form_options")
        self.button_rankings = Button(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]//2+240, texto= "RANKINGS", pantalla=pantalla,font_size=50 ,on_click=self.click_ranking, on_click_param="form_rankings")
        self.button_exit = Button(x= DIMENSION_PANTALLA[0]//2, y= DIMENSION_PANTALLA[1]//2+340, texto= "SALIR", pantalla=pantalla,font_size=50, on_click=self.click_exit)
    
        self.widget_list = [
            self.menu_ppal_title, self.menu_ppal_subtitle, self.button_start, self.button_options,
            self.button_rankings, self.button_exit
        ]

    def click_start(self, parametro):
        self.start_first_level = True
        self.set_active(parametro)
    
    def click_option(self, parametro):
        self.set_active(parametro)

    def click_ranking(self, parametro):
        self.set_active(parametro)
    
    def click_exit(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()

    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()