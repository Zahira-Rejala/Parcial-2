import pygame as pg
from .widget import Widget
from ..variables import COLOR_NEGRO

class TextTitle(Widget):

    def __init__(self, x: int, y: int, texto: str, pantalla, font_size: int = 50):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pg.font.Font("assets/fonts/light_pixel-7.ttf", self.font_size)
        self.image = self.font.render(self.texto, True, COLOR_NEGRO)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        super().draw()

    def update(self):
        self.draw()