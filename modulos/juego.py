import pygame as pg
import sys
from .forms.form_main_menu import FormMainMenu

pg.init()
from .auxiliar import (
    fondo, cartel, cartel_rect, marco, marco_rect, pregunta, pregunta_rect_uno, pregunta_rect_dos, pregunta_rect_tres,
    pregunta_rect_cuatro, pregunta_rect_cinco, pregunta_rect_seis, pregunta_rect_ocho, pregunta_rect_siete, mujer_pensando,
    mujer_pensando_rect, mesa, mesa_rect, fuente_titulo, moneda, moneda_rect, rectangulo_negro,
    rectangulo_negro_rect, fuente_dinero, half_pista, half_pista_rect, next_pista, next_pista_rect,
    reload_pista, reload_pista_rect, pregunta_dict_ocho, boton_azul, boton_rojo, boton_azul_rect, boton_rojo_rect,
    panel_preguntas, panel_preguntas_rect, cuadrado_azul, cuadrado_azul_rect, cuadrado_rojo, cuadrado_rojo_rect,
    fuente_preguntas
)

from .sonido import Sonido
from .widgets.button import Button

from .variables import (
    DIMENSION_PANTALLA, coordenada_titulo, COLOR_ROJO, SONIDO_MUSIC, COLOR_BLANCO,
    coordenada_dinero, COLOR_AZUL, COLOR_NEGRO, coordenada_prefieres
)
lista_pregunta = [pregunta_rect_uno, pregunta_rect_dos, pregunta_rect_tres,
    pregunta_rect_cuatro, pregunta_rect_cinco, pregunta_rect_seis, pregunta_rect_siete,
    pregunta_rect_ocho]


def mostrar_pregunta(lista_pregunta, pregunta, pantalla):
    for i in range(len(lista_pregunta)):
#        pg.draw.rect(pantalla, COLOR_ROJO, lista_pregunta[i])
        pantalla.blit(pregunta, lista_pregunta[i])
        


def manejador_eventos_tecla_simple(eventos, juego_corriendo: bool, sonido_juego):
    for evento in eventos:
        if evento.type == pg.QUIT:
            juego_corriendo = False
            sonido_juego.stop_musica()

        if evento.type == pg.MOUSEBUTTONDOWN:
            print(evento.pos)
    return juego_corriendo

def iniciar_juego():

    sonido_juego = Sonido()

    pantalla = pg.display.set_mode(DIMENSION_PANTALLA)

    juego_corriendo = True  

    form_mm = FormMainMenu("form_main_menu", pantalla, 0, 0, True, 1, "assets/snd/musica-menu.mp3")

    sonido_juego.play_musica(SONIDO_MUSIC)

    while juego_corriendo:

        eventos = pg.event.get()
        juego_corriendo = manejador_eventos_tecla_simple(eventos, juego_corriendo, sonido_juego)

        eventos_presionados = pg.key.get_pressed()
#        form_mm.draw()
#        form_mm.update()

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(cartel, cartel_rect)
        pantalla.blit(marco, marco_rect)


        mostrar_pregunta(lista_pregunta, pregunta, pantalla)


        pantalla.blit(mujer_pensando, mujer_pensando_rect)
        pantalla.blit(mesa, mesa_rect)
        pantalla.blit(pregunta, pregunta_rect_ocho)


        texto_titulo = fuente_titulo.render(f"THIS or THAT", True, COLOR_ROJO)
        pantalla.blit(texto_titulo, coordenada_titulo)
        pantalla.blit(rectangulo_negro, rectangulo_negro_rect)
        pantalla.blit(moneda, moneda_rect)
        contador_dinero = 0
        texto_dinero = fuente_dinero.render(f"${contador_dinero}", True, COLOR_BLANCO)
        pantalla.blit(texto_dinero, coordenada_dinero)
        pantalla.blit(panel_preguntas, panel_preguntas_rect)
        texto_preguntas = fuente_preguntas.render(f"¿Qué prefieres?", True, COLOR_NEGRO)
        pantalla.blit(texto_preguntas, coordenada_prefieres)
        pantalla.blit(next_pista, next_pista_rect)
        pantalla.blit(half_pista, half_pista_rect)
        pantalla.blit(reload_pista, reload_pista_rect)
        pantalla.blit(cuadrado_rojo, cuadrado_rojo_rect)
        pantalla.blit(cuadrado_azul, cuadrado_azul_rect)
        pantalla.blit(boton_rojo, boton_rojo_rect)
        pantalla.blit(boton_azul, boton_azul_rect)


        pg.display.flip()

    pg.quit()
    sys.exit()