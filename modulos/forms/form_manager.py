import pygame as pg
from ..variables import (
    SONIDO_MUSIC, SONIDO_MENU, SONIDO_OPCIONES, SONIDO_RANKING
    )
from .form_main_menu import FormMainMenu
from .form_ranking import FormRanking
from .form_options import FormOptions
from .form_pause import FormPause
from .form_enter_name import FormEnterName
from ..jugador import Jugador




class FormManager:
    def __init__(self, pantalla):
        self.main_screen = pantalla
        game_started = False
        self.jugador_actual = Jugador()
        self.current_level = 0
        
#        self.jugador_actual.set_puntaje(950)
        self.jugador_actual.actualizar_puntaje_total()

        self.forms = [
            FormMainMenu(name="form_main_menu", pantalla=self.main_screen, x=0, y=0, active=True, level_num=1, music_path=SONIDO_MENU),
            FormRanking(name="form_rankings", pantalla=self.main_screen, x=0, y=0, active=True, level_num=1, music_path=SONIDO_RANKING),
            FormOptions(name="form_options", pantalla=self.main_screen, x=0, y=0, active=True, level_num=1, music_path=SONIDO_OPCIONES),
            FormPause(name="form_pause", pantalla=self.main_screen, x=0, y=0, active=True, level_num=self.current_level, music_name=SONIDO_MENU),
            FormEnterName(name="form_enter_name",pantalla=self.main_screen,x=0,y=0,active=True,level_num=1,music_name=SONIDO_MENU,score=0),

        ]

#Cuando el usuario aprete ESC va al formulario pausa

    def keys_update(self, event_list: list)-> None:
        for event in event_list:
            if (event.type == pg.KEYDOWN):
                if (event.key == pg.K_ESCAPE):
                    self.forms[3].set_active("form_pause")

    def forms_update(self, event_list: list):
        if self.forms[0].active:
            self.forms[0].update()
            self.forms[0].draw()

        elif self.forms[1].active:
            self.forms[1].update()
            self.forms[1].draw()

        elif self.forms[2].active:
            self.forms[2].update()
            self.forms[2].draw()

        elif self.forms[3].active:
            self.forms[3].update()
            self.forms[3].draw()
            if self.forms[3].level_restart:
                #reinicia el nivel
                pass

        elif self.forms[4].active:
            self.forms[4].update(event_list)
            self.forms[4].draw()

    def update(self, event_list: list):
        self.keys_update(event_list)
        self.forms_update(event_list)
