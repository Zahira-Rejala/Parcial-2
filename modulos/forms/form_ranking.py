import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA
from ..auxiliar import cargar_ranking

class FormRanking(Form):
    def  __init__(self, name: str, pantalla, x: int, y: int, active: bool, level_num: int, music_path: str):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)

        self.surface = pg.image.load("assets/img/forms/ranking.jpg").convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.confirm_name = True

        self.ranking_on_screen = []
        self.ranking_list = []

        self.title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-400, texto="THIS or THAT", pantalla=pantalla, font_size=80)
        self.subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-300, texto="TOP 10 ranking", pantalla=pantalla, font_size=60)
        self.button_return_menu = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+450, texto="VOLVER AL MENU", pantalla=pantalla, on_click=self.click_return_menu, on_click_param="form_main_menu")

#        self.init_ranking()

        self.widget_list = [
            self.title, self.subtitle, self.button_return_menu
        ]
        self.music_update()

    def init_ranking(self):
        for i in range(len(self.ranking_list)):
            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2-100, y=DIMENSION_PANTALLA[1]//2.5+i*40, texto=f"{i+1}", pantalla=self.pantalla, font_size=25)
            )

            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2.5+i*40, texto=f"{self.ranking_list[i][0]}", pantalla=self.pantalla, font_size=25)
            )

            self.ranking_on_screen.append(
                TextTitle(x=DIMENSION_PANTALLA[0]//2+100, y=DIMENSION_PANTALLA[1]//2.5+i*40, texto=f"{self.ranking_list[i][1]}", pantalla=self.pantalla, font_size=25)
            )            

    def inicializar_ranking(self):
        self.ranking_list = cargar_ranking()
        self.init_ranking()

    def click_return_menu(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
        for ranking in self.ranking_on_screen:
            ranking.draw()
        
    def update(self):
        if self.active:
            self.inicializar_ranking()
        super().draw()
        for widget in self.widget_list:
            widget.update()