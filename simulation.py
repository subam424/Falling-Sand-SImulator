import pygame
from components import Simulation

pygame.init()

# CONSTANTS 
WIDTH = 1000
HEIGHT = 700
FPS = 120
BG = (29, 29, 29)
CELL_SIZE = 7
FONT = pygame.font.SysFont("arial", 20)
LINE_1 = FONT.render("C - Create [ S - Sand | R - Rock | W - Water ]", True, (255, 255, 255))
LINE_2 = FONT.render("E - Eraser | SPACE - Reset", True, (255, 255, 255))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand")
clock = pygame.time.Clock()
simulation = Simulation(WIDTH, HEIGHT, CELL_SIZE)

# MAIN LOOP
while True:
    simulation.handle_events()

    simulation.update()

    simulation.draw(screen, BG)
    screen.blit(LINE_1, (10, 10))
    screen.blit(LINE_2, (10, 35))
    pygame.display.flip()
    clock.tick(FPS) 