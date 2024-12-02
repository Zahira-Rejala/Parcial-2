import pygame as pg
from .auxiliar import achicar_imagen
from .variables import RUTA_MUJER_PENSANDO

class Jugador:

    __instanciado = None

    def  __init__(self, nombre: str = "Jugador 1", pos_x: int = 0, pos_y: int = 0):

        if Jugador.__instanciado is None:
            Jugador.__instanciado = self

        self.nombre = nombre
        self.puntaje = 0
        self.puntaje_total = 0
        self.imagen = achicar_imagen(RUTA_MUJER_PENSANDO, 6)
        self.rect = self.imagen.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    @staticmethod
    def get_jugador():
        if Jugador.__instanciado is None:
            Jugador()
        return Jugador.__instanciado
    
    @staticmethod
    def esta_instanciado():
        return Jugador.__instanciado != None

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_puntaje_actual(self):
        return self.puntaje
    
    def get_puntaje_total(self):
        return self.puntaje_total
    
    def to_csv_format(self):
        return f"\n{self.nombre},{self.puntaje_total}"

    def set_puntaje(self, puntaje: int):
        self.puntaje = puntaje

    def add_puntaje(self, puntaje: int):
        self.puntaje += puntaje
    
    def actualizar_puntaje_total(self):
        self.puntaje_total += self.puntaje

    def events(self, lista_eventos:list):
        pass

    def draw(self, screen):
        screen.blit(self.imagen, self.rect)
    
    def update(self, lista_eventos):
        self.events(lista_eventos)