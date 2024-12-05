import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..jugador import Jugador
from ..nivel import Nivel
from ..variables import DIMENSION_PANTALLA, coordenada_dinero, FPS



class FormJuego(Form):
    def __init__(self, name: str, pantalla, x: int, y: int, active: bool, level_num: int, music_path: str):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        self.level_restart = False
        self.advance_level = False
        self.level_timer = 60
        self.actual_level = level_num
        self.timer_detener = False

        self.first_last_timer = pg.time.get_ticks()

        self.music_update()

        self.jugador = Jugador.get_jugador()
        from ..auxiliar import pregunta
        from ..juego import lista_pregunta
        self.level = Nivel(self.actual_level, self.pantalla, lista_pregunta, pregunta)

        self.clock = pg.time.Clock()

        self.puntaje_title = TextTitle(x=130, y=165, texto=f"{self.level.get_puntaje()}", pantalla=self.pantalla, font_size=30)
        self.info_timer = TextTitle(x=400, y=200, texto=f"Tiempo: {self.level_timer}", pantalla=self.pantalla, font_size=20)
        self.widget_list = [self.puntaje_title, self.info_timer]

    def draw(self):
        self.level.draw()
        for widget in self.widget_list:
            widget.draw()

    def actualizar_timer(self):
        if self.level_timer > 0 and not self.timer_detener:
            tiempo_actual = pg.time.get_ticks()
            if (tiempo_actual - self.first_last_timer) > 1000:
                self.level_timer -= 1
                self.first_last_timer = tiempo_actual

    def restart_level(self):
        self.level_restart = True
        self.jugador = Jugador.get_jugador()
        self.jugador.set_puntaje(0)
        self.level = Nivel(self.actual_level, self.pantalla)
        for item in self.level.items:
            for item in self.level.items:
                item["visible"] = True

    def level_advance(self):
        if self.level.nivel_ganado() and self.level_timer > 0:
            self.advance_level = True
            print("Nivel ganado!")
            self.set_active("form_enter_name")
        elif self.level_timer == 0:
            self.set_active("form_enter_name")
            
    def update(self):

        self.widget_list[0] = TextTitle(x=400, y=200, texto=f"Tiempo: {self.level_timer}", pantalla=self.pantalla, font_size=20)
        self.widget_list[1] = TextTitle(x=170, y=210, texto=f"${self.level.get_puntaje()}", pantalla=self.pantalla, font_size=40)

        self.clock.tick(FPS)
#        keys_event = pg.key.get_pressed()
#        self.level.update(keys_event)
        self.actualizar_timer()

