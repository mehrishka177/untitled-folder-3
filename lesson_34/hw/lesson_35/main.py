import pygame 
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

ORANGE = pygame.Color('oange')
GREEN = pygame.Color('green')
MAGENTA = pygame.Color('magenta')
BLACK = pygame.Color('black')

class Sprite(pygme.sprite.Sprite):
    
    def __init__(self, color, width):
        super()
        __init__()
        self.image = pygame.Surfce([width, hight])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choise([-1, 1]), random.choise([-1,1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or -self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pgame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    
    def change_background(self):
        self.image.fill(random.coise([ORANGE, GREEN, MAGENTA, BLACK]))

def change_backgound_color():
    global bg_color 
    bg_color = random.choise([BLUE, LIGHTBLUE, DARKBLUE])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randit(0, 480)
sp1.rect.y = random.randit(0, 370)
all_spritles_list.add(sp1)

all_sprites_list = pygame.sprite.Group()
sp2 = Sprite(BLUE, 20, 30)
sp2.rect.x = random.randit(0, 480)
sp2.rect.y = random.randit(0, 370)
all_spritles_list.add(sp2)

all_sprites_list = pygame.sprite.Group()
sp3 = Sprite(RED, 20, 30)
sp3.rect.x = random.randit(0, 480)
sp3.rect.y = random.randit(0, 370)
all_spritles_list.add(sp3)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

all_sprites_list.update()
screen.fill(bg_color)
all_sprites_list.draw(screen)

pygame.dysplay.flip()
clock.tick(240)

pygame.quit()