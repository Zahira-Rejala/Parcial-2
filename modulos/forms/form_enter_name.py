import pygame as pg
from .form import Form
from ..widgets import Button, TextBox, TextTitle
from ..variables import DIMENSION_PANTALLA
from ..jugador import Jugador
from ..auxiliar import grabar_puntaje

class FormEnterName(Form):
    '''
    This class represents the enter name form  
    '''
    def __init__(self,name:str,pantalla:object,x:int,y:int,active:bool,level_num:int,music_name:str,score:int)->None:
        super().__init__(name,pantalla,x,y,active,level_num,music_name)

        self.surface = pg.image.load('./assets/img/forms/enter-name.jpg').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.jugador = Jugador.get_jugador()
        self.score = self.jugador.get_puntaje_total()
        
        self.music_update()
        self.confirm_name = False
        
        self.title = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-300,texto="This or That",pantalla=pantalla,font_size=75)
        self.subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-100,texto="INGRESE SU NOMBRE:",pantalla=pantalla,font_size=50)
        self.subtitle_score = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-20,texto=f"PUNTAJE:{self.score}",pantalla=pantalla,font_size=30)
        
        self.text_box = TextBox(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+60,texto="_________________",pantalla=pantalla)
        self.button_confirm_name = Button(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+100,texto="CONFIRMAR NOMBRE",pantalla=pantalla
        ,on_click=self.click_confirm_name)
        
        self.widget_list = [self.title,self.subtitle,self.subtitle_score,self.button_confirm_name]

        
    def click_confirm_name(self,parametro:str)->None: 
        '''
        Sets confirm name flag as True 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.confirm_name = True
        self.jugador.set_nombre(self.writing_text.texto)
        print(f'Su nombre: {self.jugador.get_nombre()} - {self.jugador.get_puntaje_total()} puntos')
        grabar_puntaje(self.jugador)
        self.set_active('form_rankings')
        
    def draw(self)->None:
        '''
        Merges the elements of the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        self.text_box.draw()
        self.writing_text  = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+30,texto=f"{self.text_box.writing.upper()}",
        pantalla=self.pantalla,font_size=30)
        self.writing_text.draw()

    def update(self,event_list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        self.text_box.update(event_list)
        for widget in self.widget_list:    
            widget.update()  
