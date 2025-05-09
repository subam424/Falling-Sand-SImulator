import pygame
from components import Simulation

pygame.init()

# CONSTANTS 
WIDTH = 1000
HEIGHT = 700
FPS = 120
BG = (29, 29, 29)
CELL_SIZE = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand")
clock = pygame.time.Clock()
simulation = Simulation(WIDTH, HEIGHT, CELL_SIZE)

# MAIN LOOP
while True:
    simulation.handle_events()

    simulation.update()

    # DRAW THE SCREEN
    simulation.draw(screen, BG)

    pygame.display.flip()
    clock.tick(FPS)