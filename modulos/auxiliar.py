import pygame as pg
pg.init()

import json
from .variables import (
    RUTA_FONDO, RUTA_CARTELES, RUTA_PREGUNTA, coordenada_carteles, RUTA_MARCO, coordenada_marco, coordenada_pregunta_uno,
    coordenada_pregunta_dos, coordenada_pregunta_tres, coordenada_pregunta_cuatro, coordenada_pregunta_cinco,
    coordenada_pregunta_seis, coordenada_pregunta_siete, coordenada_pregunta_ocho, RUTA_MUJER_PENSANDO, coordenada_mujer_pensando,
    RUTA_MESA, coordenada_mesa, RANKING_FILE, CONFIGS_FILE, RUTA_MONEDA, coordenada_moneda,
    RUTA_RECTANGULO_NEGRO, coordenada_rectangulo_negro, RUTA_HALF, RUTA_NEXT, RUTA_RELOAD,
    coordenada_next, coordenada_half, coordenada_reload, RUTA_BOTON_AZUL, RUTA_BOTON_ROJO, coordenadas_boton_azul,
    coordenadas_boton_rojo, RUTA_PANEL_PREGUNTAS, coordenadas_panel_preguntas, RUTA_CUADRADO_ROJO, RUTA_CUADRADO_AZUL,
    coordenada_cuadrado_azul, coordenada_cuadrado_rojo
)

def achicar_imagen(ruta_imagen: str, cantidad: int) -> pg.surface:
    imagen_raw = pg.image.load(ruta_imagen)
    alto = imagen_raw.get_height() // cantidad
    ancho = imagen_raw.get_width() // cantidad
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final

def crear_diccionario_item(sup_imagen:pg.Surface, sup_rect: pg.Rect) -> dict:
    objeto = {
        "imagen": sup_imagen,
        "rect": sup_rect,
        "visible": True
    }
    return objeto

def sort_matrix(matrix: list[list]):
    for i in range(len(matrix) - 1):
        for j in range(i+1, len(matrix)):
            if int(matrix[i][1]) < int(matrix[j][1]):
                matrix[i], matrix[j] = matrix[j], matrix[i]
    


def cargar_ranking():
    ranking = []
    with open(RANKING_FILE, 'r') as rkng:
        lineas = rkng.read()
        for linea in lineas.split('\n'):
            ranking.append(linea.split(','))
    sort_matrix(ranking)
    return ranking

def grabar_puntaje(jugador):
    with open(RANKING_FILE, "+a") as rkn:
        rkn.write(jugador.to_csv_format())
        print("Puntaje guardado con éxito!")

def cargar_configs():
    configuraiones = {}
    with open(CONFIGS_FILE, "r") as configs:
        configuraiones = json.load(configs)
    return configuraiones


def grabar_puntaje(jugador):
    with open(RANKING_FILE, '+a') as rkn:
        rkn.write(jugador.to_csv_format())
        print('PUNTAJE GUARDADO CON ÉXITO!')


cartel = achicar_imagen(RUTA_CARTELES, 2.50)
cartel_rect = pg.Rect(coordenada_carteles, cartel.get_size())
marco = achicar_imagen(RUTA_MARCO, 2.17)
marco_rect = pg.Rect(coordenada_marco, marco.get_size())
moneda = achicar_imagen(RUTA_MONEDA, 15)
moneda_rect = pg.Rect(coordenada_moneda, moneda.get_size())
rectangulo_negro = achicar_imagen(RUTA_RECTANGULO_NEGRO, 4)
rectangulo_negro_rect = pg.Rect(coordenada_rectangulo_negro, rectangulo_negro.get_size())
#pistas
next_pista = achicar_imagen(RUTA_NEXT, 5)
next_pista_rect = pg.Rect(coordenada_next, next_pista.get_size())
half_pista = achicar_imagen(RUTA_HALF, 1.4)
half_pista_rect = pg.Rect(coordenada_half, half_pista.get_size())
reload_pista = achicar_imagen(RUTA_RELOAD, 5)
reload_pista_rect = pg.Rect(coordenada_reload, reload_pista.get_size())

boton_rojo = achicar_imagen(RUTA_BOTON_ROJO, 4)
boton_rojo_rect = pg.Rect(coordenadas_boton_rojo, boton_rojo.get_size())
boton_azul = achicar_imagen(RUTA_BOTON_AZUL,3.5)
boton_azul_rect = pg.Rect(coordenadas_boton_azul, boton_azul.get_size())

panel_preguntas = achicar_imagen(RUTA_PANEL_PREGUNTAS, 4.5)
panel_preguntas_rect = pg.Rect(coordenadas_panel_preguntas, panel_preguntas.get_size())

cuadrado_rojo = achicar_imagen(RUTA_CUADRADO_ROJO, 2.1)
cuadrado_rojo_rect = pg.Rect(coordenada_cuadrado_rojo, cuadrado_rojo.get_size())
cuadrado_azul = achicar_imagen(RUTA_CUADRADO_AZUL, 3)
cuadrado_azul_rect = pg.Rect(coordenada_cuadrado_azul, cuadrado_azul.get_size())

pregunta = achicar_imagen(RUTA_PREGUNTA, 8.5)

pregunta_rect_uno = pg.Rect(coordenada_pregunta_uno, pregunta.get_size())
pregunta_dict_uno = crear_diccionario_item(pregunta, pregunta_rect_uno)

pregunta_rect_dos = pg.Rect(coordenada_pregunta_dos, pregunta.get_size())
pregunta_dict_dos = crear_diccionario_item(pregunta, pregunta_rect_dos)

pregunta_rect_tres = pg.Rect(coordenada_pregunta_tres, pregunta.get_size())
pregunta_dict_tres = crear_diccionario_item(pregunta, pregunta_rect_tres)

pregunta_rect_cuatro = pg.Rect(coordenada_pregunta_cuatro, pregunta.get_size())
pregunta_dict_cuatro = crear_diccionario_item(pregunta, pregunta_rect_cuatro)

pregunta_rect_cinco = pg.Rect(coordenada_pregunta_cinco, pregunta.get_size())
pregunta_dict_cinco = crear_diccionario_item(pregunta, pregunta_rect_cinco)

pregunta_rect_seis = pg.Rect(coordenada_pregunta_seis, pregunta.get_size())
pregunta_dict_seis = crear_diccionario_item(pregunta, pregunta_rect_seis)

pregunta_rect_siete = pg.Rect(coordenada_pregunta_siete, pregunta.get_size())
pregunta_dict_siete = crear_diccionario_item(pregunta, pregunta_rect_siete)

pregunta_rect_ocho = pg.Rect(coordenada_pregunta_ocho, pregunta.get_size())
pregunta_dict_ocho = crear_diccionario_item(pregunta, pregunta_rect_ocho)



mujer_pensando = achicar_imagen(RUTA_MUJER_PENSANDO, 6)
mujer_pensando_rect = pg.Rect(coordenada_mujer_pensando, mujer_pensando.get_size())
mesa = achicar_imagen(RUTA_MESA, 2)
mesa_rect = pg.Rect(coordenada_mesa, mesa.get_size())




fondo_raw = pg.image.load(RUTA_FONDO)
fondo = pg.transform.scale(fondo_raw, (1920, 1200))

fuente_titulo = pg.font.Font("./assets/fonts/BungeeTint-Regular.ttf", 70) 
fuente_dinero = pg.font.Font("./assets/fonts/pixeldown.ttf", 30)
fuente_preguntas = pg.font.Font("./assets/fonts/Modak-Regular.ttf", 35)