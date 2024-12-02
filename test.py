import pygame as pg
pg.init()

from modulos.jugador import Jugador


jugador_1 = Jugador(nombre="Jugador de prueba")
print(jugador_1.get_nombre())