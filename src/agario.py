import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    actual_surface = pygame.display.get_surface()
    center_x = actual_surface.get_width()/2
    center_y = actual_surface.get_height()/2

    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (center_x, center_y), 50, 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
