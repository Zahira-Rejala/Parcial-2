import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA

class FormOptions(Form):
    def __init__(self, name: str, pantalla, x: int, y: int, active: bool, level_num: int, music_path: str):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.surface = pg.image.load("assets/img/forms/opciones.jpg").convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)

        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y


        self.optiones_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-400, texto="THIS or THAT", pantalla=pantalla, font_size=80)
        self.optiones_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-300, texto="OPCIONES", pantalla=pantalla, font_size=60)
        self.button_music_on = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-100, texto="MUSIC ON", pantalla=pantalla, on_click=self.click_music_on)
        self.button_music_off = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+100, texto="MUSIC OFF", pantalla=pantalla, on_click=self.click_music_off)
        self.button_back = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+250, texto="VOLVER AL MENU", pantalla=pantalla, on_click=self.click_back, on_click_param="form_main_menu")
        self.widgets_list = [
            self.optiones_subtitle, self.optiones_title, self.button_back, self.button_music_off,
            self.button_music_on
        ]
        self.music_update()


    def click_music_on(self, parametro):
        pg.mixer.music.unpause()
    
    def click_music_off(self, parametro):
        pg.mixer.music.pause()
    
    def click_back(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widgets_list:
            widget.update()        
