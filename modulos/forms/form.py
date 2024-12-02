from ..sonido import Sonido

class Form:

    forms_dict = {}

    def __init__(self, name:str, pantalla, x: int, y: int, active: bool, level_num: int, music_path:str):
        self.forms_dict[name] = self
        self.pantalla = pantalla
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_path = music_path
        self.admin_sonido = Sonido()

    def set_active(self, name: str):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True
    
    def music_update(self):
        self.admin_sonido.stop_musica()
        self.admin_sonido.play_musica(f"{self.music_path}")

    def draw(self):
        self.pantalla.blit(self.surface, self.slave_rect)