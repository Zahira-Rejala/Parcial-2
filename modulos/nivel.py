import pygame as pg
from .jugador import Jugador
from .auxiliar import (
    cargar_configs, pregunta_dict_uno, pregunta_dict_dos, boton_rojo_dict,
    boton_azul_dict, cartel, cartel_rect, marco, marco_rect, pregunta, panel_preguntas, panel_preguntas_rect,
    fuente_preguntas, cuadrado_azul, cuadrado_azul_rect, cuadrado_rojo, cuadrado_rojo_rect, rectangulo_negro,
    rectangulo_negro_rect, moneda, moneda_rect, boton_azul, boton_azul_rect, boton_rojo, boton_rojo_rect,
    crear_diccionario_item, pregunta_rect_ocho
    )
from .variables import (
    DIMENSION_PANTALLA, coordenada_prefieres, COLOR_NEGRO, coordenada_respuesta_uno, 
    coordenada_respuesta_dos, coordenadas_boton_rojo, RUTA_BOTON_ROJO, coordenadas_boton_azul, COLOR_ROJO,
    COLOR_AZUL, FPS
    )
import random


class Button:
    def __init__(self, rect, color, text, callback):
        """
        Inicializa un botón.

        Args:
        - rect (pg.Rect): El rectángulo que define la posición y tamaño del botón.
        - color (tuple): Color del botón (RGB).
        - text (str): Texto que se muestra en el botón.
        - callback (function): Función a ejecutar cuando el botón es presionado.
        """
        self.rect = rect
        self.color = color
        self.text = text
        self.callback = callback
        self.font = pg.font.Font(None, 36)  # Fuente por defecto para el texto

    def event(self,evento):
        if evento.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):  # Verifica si el clic ocurrió en el botón
                if callable(self.callback):       # Si el callback es ejecutable, lo llama
                    self.callback()            
        

    def draw(self, pantalla):
        # Dibuja el botón como un rectángulo
        pg.draw.rect(pantalla, self.color, self.rect)
        # Dibuja el texto centrado en el rectángulo
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        pantalla.blit(text_surface, text_rect)


class Nivel:
    def __init__(self, nro_nivel: int, pantalla, lista_pregunta, pregunta):
        self.nro_nivel = nro_nivel
        self.pantalla = pantalla        
        self.configs = {}
        self.items = []
        self.nivel_terminado = False
        self.jugador = Jugador.get_jugador()
        self.cargar_configs()
        self.lista_pregunta = lista_pregunta
        self.pregunta = pregunta
        self.pregunta_rect_ocho = pregunta_rect_ocho

        self.surface = pg.image.load(f"assets/img/{self.configs.get('fondo')}").convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = 0
        self.slave_rect.y = 0

        self.puntaje_nivel = 0

        self.objetos_cuadrados = None
        self.boton_azul = boton_azul
        self.boton_azul_rect = boton_azul_rect
        self.boton_rojo_rect = boton_rojo_rect
        self.mostrar_rectangulo_rojo = False
        self.mostrar_rectangulo_azul = False
        self.tiempo_click = 0
        self.reloj = pg.time.Clock()




            
    def desaparecer(self, pregunta, lista_pregunta):
        invisible = crear_diccionario_item(pregunta, lista_pregunta)
        invisible["visible"] = False

    def get_puntaje(self):
        return self.puntaje_nivel
    
    def cargar_configs(self):
        configs_globales = cargar_configs()
        self.configs = configs_globales.get(f"nivel_{self.nro_nivel}")

    def draw_tribuna(self):
        self.pantalla.blit(cartel, cartel_rect)
        self.pantalla.blit(marco, marco_rect)
        from .juego import lista_pregunta, mostrar_pregunta
        mostrar_pregunta(lista_pregunta, pregunta, self.pantalla)

    def draw_botones(self):
        self.pantalla.blit(boton_rojo, boton_rojo_rect)
        self.pantalla.blit(boton_azul, boton_azul_rect)

    def draw_prefieres(self):
        self.pantalla.blit(panel_preguntas, panel_preguntas_rect)
        texto_preguntas = fuente_preguntas.render(f"¿Qué prefieres?", True, COLOR_NEGRO)
        self.pantalla.blit(texto_preguntas, coordenada_prefieres)

    def draw_preguntas(self):
        self.pantalla.blit(cuadrado_rojo, cuadrado_rojo_rect)
        self.pantalla.blit(cuadrado_azul, cuadrado_azul_rect)
        texto = fuente_preguntas.render(self.configs.get("answer")[0], True, COLOR_NEGRO)
        texto_dos = fuente_preguntas.render(self.configs.get("answer")[1], True, COLOR_NEGRO)
        
        if self.nro_nivel == 1:
            self.pantalla.blit(texto, coordenada_respuesta_uno)
            self.pantalla.blit(texto_dos, coordenada_respuesta_dos)

    def draw_monedas(self):
        self.pantalla.blit(rectangulo_negro, rectangulo_negro_rect)
        self.pantalla.blit(moneda, moneda_rect)


    def preguntas_completadas(self):
        pass

    def nivel_ganado(self):
        gana = (self.preguntas_completadas() == True)

    def actualizar_puntaje(self):
        self.puntaje_nivel += 20
        self.jugador.set_nombre(self.puntaje_nivel)

    def draw_player(self):
        self.jugador.draw(self.pantalla)
    
    def draw_nivel(self):
        self.pantalla.blit(self.surface, self.slave_rect)

    def cuadrados_aleatorios(self):
        if self.objetos_cuadrados is None:
            self.objetos_cuadrados = []
            colores = [COLOR_AZUL, COLOR_ROJO]

            for rect in self.lista_pregunta:
                color = random.choice(colores)
                objeto = {
                    "imagen": pregunta,
                    "rect": rect,
                    "color": color,
                    "visible": True
                }
                self.objetos_cuadrados.append(objeto)

        for objeto in self.objetos_cuadrados:
            if objeto["visible"]:
                pg.draw.rect(self.pantalla, objeto["color"], objeto["rect"])
            

    def click(self, lista_eventos, detener_timer_callback):
        for evento in lista_eventos:
            if evento.type == pg.MOUSEBUTTONDOWN: 
                if self.boton_rojo_rect.collidepoint(evento.pos):
                    if detener_timer_callback:
                        detener_timer_callback()
                    pg.draw.rect(self.pantalla, COLOR_ROJO, self.pregunta_rect_ocho)
                    self.mostrar_rectangulo_rojo = True
                    self.tiempo_click = pg.time.get_ticks()
                    tiempo_transcurrido = pg.time.get_ticks() - self.tiempo_click
                    if tiempo_transcurrido > 5000: 
                        self.mostrar_rectangulo_rojo = False
                if self.boton_azul_rect.collidepoint(evento.pos):
                    if detener_timer_callback:
                        detener_timer_callback()
                    pg.draw.rect(self.pantalla, COLOR_AZUL, self.pregunta_rect_ocho)
                    self.mostrar_rectangulo_azul = True
                    self.tiempo_click = pg.time.get_ticks()
                    tiempo_transcurrido = pg.time.get_ticks() - self.tiempo_click
                    if tiempo_transcurrido > 5000: 
                        self.mostrar_rectangulo_rojo = False
        # pg.display.flip()
        # self.reloj.tick(30)
    def update(self):
        def detener_timer():
            self.timer_detener = True  # Detiene el temporizador

        self.level.update(detener_timer_callback=detener_timer)
        self.actualizar_timer()
        self.draw()
#                elif self.boton_azul.collidepoint(evento.pos):
#                    pg.draw.rect(self.pantalla, COLOR_AZUL, self.pregunta_rect_ocho)





    def draw(self):
        self.draw_nivel()
        self.draw_monedas()
        self.draw_tribuna()
        self.draw_player()
        self.draw_prefieres()
        self.draw_preguntas()
        self.draw_botones()
        if self.mostrar_rectangulo_rojo:
            pg.draw.rect(self.pantalla, COLOR_ROJO, self.pregunta_rect_ocho)
            tiempo_transcurrido = pg.time.get_ticks() - self.tiempo_click
            if tiempo_transcurrido > 5000:  
                self.mostrar_rectangulo_rojo = False  
        self.cuadrados_aleatorios()
        pg.display.flip()  # Actualiza la pantalla
    
    def update(self, eventos: list,detener_timer_callback= None):
        self.jugador.update(lista_eventos=eventos)
        self.click(eventos, detener_timer_callback)
        self.draw()
    

