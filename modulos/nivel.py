import pygame as pg
from .jugador import Jugador
from .auxiliar import cargar_configs, pregunta_dict_uno, pregunta_dict_dos
from .variables import DIMENSION_PANTALLA

class Nivel:
    def __init__(self, nro_nivel: int):
        self.nro_nivel = nro_nivel
        self.configs = {}
        self.items = []
        self.nivel_terminado = False
        self.jugador = Jugador.get_jugador()
        self.cargar_configs()
        self.crear_items()

        self.surface = pg.image.load(f"assets/img/{self.configs.get("fondo")}").convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = 0
        self.slave_rect.y = 0        
    
    def cargar_configs(self):
        configs_globales = cargar_configs()
        self.configs = configs_globales.get(f"nivel_{self.nro_nivel}")

    def crear_items(self):
        for item in self.configs.get("items"):
            match item:
                case "pregunta":
                    item_nivel = pregunta_dict_uno
            self.items.append(item_nivel)

    def draw_items(self, pantalla):
        for item in self.items:
            if item.get("visible"):
                pantalla.blit(item.get("imagen"), item.get("rect"))

    # def hay_items_visibles(self):
    #     for item in self.items:
    #         if item.get("visible")



    def draw_player(self, pantalla):
        self.jugador.draw(pantalla)
    
    def draw_nivel(self, pantalla):
        pantalla.blit(self.surface, self.slave_rect)

    def draw(self):
        self.draw_nivel()
        self.draw_items()
        self.draw_player()
    
    def update(self):
        pass