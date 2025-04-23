import pygame
from pygame.sprite import Sprite
from menu_state import MenuState

class Button(Sprite):
    def __init__(self, name, tex):
        Sprite.__init__(self)
        self.name = name
        self.image = tex
        self.rect = self.image.get_rect()
        self.down = False
        self.state: str = ""
        
        self.pressed = False

    def update(self, mouse_pos: pygame.math.Vector2, mouse_down: bool):
            self.pressed = False

            if not mouse_down:
                 self.down = False
                 return
            
            current_state = (mouse_pos.x > self.rect.x and mouse_pos.x < self.rect.x + self.rect.width) \
                        and (mouse_pos.y > self.rect.y and mouse_pos.y < self.rect.y + self.rect.height)

            if not self.down and current_state:
                 self.pressed = True

            self.down = current_state

            if self.pressed:
                print(f"Pressed {self.name}")
 