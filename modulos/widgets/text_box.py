import pygame as pg
from .widget import Widget
from ..variables import COLOR_AZUL

class TextBox(Widget):
    
    def __init__(self, x: int, y: int, texto: str, pantalla, font_size: int = 25, on_click = None, on_click_param = None):
        super().__init__(x, y, texto, pantalla, font_size)
        self.font = pg.font.Font("./assets/fonts/Modak-Regular.ttf", self.font_size)
        self.image = self.font.render(self.texto, True, COLOR_AZUL)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click_option_sfx = pg.mixer.Sound("assets/snd/click.mp3")

        self.on_click = on_click
        self.on_click_param = on_click_param

        self.write_on = True
        self.writing = ""
        self.image_writing = self.font.render(self.writing, True, COLOR_AZUL)
        self.rect_writing = self.image_writing.get_rect()
        self.rect_writing.center = (x, y)

    def write_on_box(self, event_list: list):
        for evento in event_list:
            if evento.type == pg.KEYDOWN and self.write_on:
                if evento.key == pg.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += evento.unicode
    def draw(self):
        super().draw()
        self.image.blit(self.pantalla, (self.rect_writing.x, self.rect_writing.y))

    def update(self, event_list: list):
        self.draw()
        self.write_on_box(event_list)