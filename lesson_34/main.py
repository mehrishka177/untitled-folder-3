import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygae.draw.rect(screen, (o, 125, 255), pygame.Rect(30, 30, 60, 60))
    
    pygame.display.flip()
    
