import pygame
import mpmath
import math

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

actual_surface = pygame.display.get_surface()
cell_x = actual_surface.get_width()/2
cell_y = actual_surface.get_height()/2
max_x = actual_surface.get_width()
max_y = actual_surface.get_height()

velocity = 1

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 

    mouse_pos = pygame.mouse.get_pos()
    dir_x = mouse_pos[0] - cell_x
    dir_y = mouse_pos[1] - cell_y

    diff_x = math.fabs(cell_x-mouse_pos[0])
    diff_y = math.fabs(cell_y-mouse_pos[1])

    distance = math.sqrt( (diff_x)**2 + (diff_y)**2 )
    increment_x = velocity*math.sin( diff_x/distance )
    increment_y = velocity*math.cos( diff_x/distance )
    if dir_x > 0:
        cell_x = cell_x + increment_x
    else:
        cell_x = cell_x - increment_x

    if dir_y > 0:
        cell_y = cell_y + increment_y
    else:
        cell_y = cell_y - increment_y


    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, ( int(cell_x), int(cell_y) ), 50, 0)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
