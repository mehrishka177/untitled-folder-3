import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates

clock = pygame.time.Clock()



while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [300, 200, 100, 100],0)
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [300, 200, 100, 100],0)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()