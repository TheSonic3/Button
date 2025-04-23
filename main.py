import pygame
from button import Button
from menu_state import MenuState

# Initialize pygame:q

pygame.init()
clock = pygame.time.Clock()

# Screen dimensions
height = 900
base = 1200
screen = pygame.display.set_mode((base, height))
pygame.display.set_caption('Base')


# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHTGRAY = (200, 200, 200)
DARKPURPLE = (128, 0, 128)
ikerColour = [0, 255, 0]

#Initial conditions defined
rectPos = pygame.math.Vector2(0, 0)
rectWidth = 580
rectHeight = 450
rectanglyDim = pygame.math.Vector2(100, 40)
playerPos = pygame.math.Vector2(50,50)
playerWidth = 300
playerHeight = 250
buttonList = []
playerRectList = []
collisionRectList = []
mouseRadius = 1
mousePos = pygame.math.Vector2(pygame.mouse.get_pos())
clickValue = False
menu_state: MenuState = MenuState.MAIN

button_states = {
    "attack": "",
    "items": "",
    "run": "",
    "swap": "",
}

# Define the initial 4 rectangles
class RectVal:
    def __init__(self, value, name, hidden=False):
        self.value = value  # pygame.Rect
        self.name = name
        self.hidden = hidden

class Player(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        # Load and scale the image for Player
        self.image = pygame.transform.scale(pygame.image.load('Square4.png').convert_alpha(), (playerWidth, playerHeight))
        # Set the position of Rect4 (offset from Rect1)
        self.rect = self.image.get_rect(topleft=(playerPos.x + 700, playerPos.y + 580))
    def update (self):
        self.checkCollisions()
        pass
    def checkCollisions (self):
        pass

def update_menu(mouse_down: bool):
    mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
    for button in buttons.sprites():
        button.update(mouse_pos, mouse_down)
        if button.pressed:

buttons = pygame.sprite.Group()

ref_image = pygame.image.load("Square1.png")
for i in range(4):
    image = pygame.transform.scale(pygame.image.load(f"Square{i + 1}.png"), (ref_image.width, ref_image.height))
    button = Button(f"Button {i + 1}", image)
    buttons.add(button)


print(f"#rects = {len(buttons)}")
buttonList: list[Button] = buttons.sprites()


buttonList[1].rect.x = screen.width - buttonList[1].rect.width
buttonList[1].rect.y = 0

buttonList[2].rect.x = 0
buttonList[2].rect.y = screen.height - buttonList[2].rect.height
buttonList[2].rect.width = buttonList[0].rect.width
buttonList[2].rect.height = buttonList[0].rect.height

buttonList[3].rect.x = screen.width - buttonList[3].rect.width
buttonList[3].rect.y = screen.height - buttonList[3].rect.height

running: bool = True
mouse_down: bool = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        mouse_down = event.type == pygame.MOUSEBUTTONDOWN
    
    if not running:
        break

    buttons.draw(screen)
    dt = clock.get_time() / 1000
    update_menu(mouse_down)
    pygame.display.flip()

pygame.quit()

