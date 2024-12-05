import sys
import pygame as pg
from modulos.forms.form_manager import (
    FormManager
)
from modulos.variables import DIMENSION_PANTALLA
from modulos.auxiliar import cargar_ranking

def manejador_eventos_tecla_simple(eventos, juego_corriendo: bool):
    for evento in eventos:
        if evento.type == pg.QUIT:
            juego_corriendo = False
        # if evento.type == pg.MOUSEBUTTONDOWN:
        #     print(evento.pos)
    return juego_corriendo

def run_game():
    pg.init()
    pantalla_ppal = pg.display.set_mode(DIMENSION_PANTALLA, pg.SCALED)
    pg.display.set_caption("THIS or THAT")
    
    run = True

    
    forms = FormManager(pantalla_ppal)
    from .nivel import Nivel
    nivel = Nivel(1, pantalla_ppal, lista_pregunta=[], pregunta=None)

    while run:

        eventos = pg.event.get()
        run = manejador_eventos_tecla_simple(eventos, run)
        nivel.update(eventos)
        eventos_presionados = pg.key.get_pressed()
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                run = False
        
        forms.update(event_list)
        pg.display.update()
    pg.quit()
    sys.exit()