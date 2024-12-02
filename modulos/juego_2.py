import sys
import pygame as pg
from modulos.forms.form_manager import (
    FormManager
)
from modulos.variables import DIMENSION_PANTALLA
from modulos.auxiliar import cargar_ranking

def run_game():
    pg.init()
    pantalla_ppal = pg.display.set_mode(DIMENSION_PANTALLA, pg.SCALED)
    pg.display.set_caption("THIS or THAT")
    
    run = True
    
    forms = FormManager(pantalla_ppal)

    while run:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                run = False
        
        forms.update(event_list)
        pg.display.update()
    pg.quit()
    sys.exit()