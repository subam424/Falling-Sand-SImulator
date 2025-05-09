import pygame
import sys
from components import Simulation, SandParticle, Water

pygame.init()

# CONSTANTS 
WIDTH = 1000
HEIGHT = 700
FPS = 120
BG = (29, 29, 29)
CELL_SIZE = 8
particle_type = SandParticle
action = "create"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Sand")
clock = pygame.time.Clock()
simulation = Simulation(WIDTH, HEIGHT, CELL_SIZE)

# MAIN LOOP
while True:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation.reset()
            elif event.key == pygame.K_s:
                particle_type = SandParticle
            elif event.key == pygame.K_w:
                particle_type = Water
            elif event.key == pygame.K_c:
                action = "create"
            elif event.key == pygame.K_e:
                action = "erase"
        
    clicks = pygame.mouse.get_pressed()
    if clicks[0]:
        x, y = pygame.mouse.get_pos()
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        if action == "create":
            simulation.add_particle(row, col, particle_type)
        elif action == "erase":
            simulation.erase_particle(row, col)

    simulation.update()

    # DRAW THE SCREEN
    simulation.draw(screen, BG)

    pygame.display.flip()
    clock.tick(FPS)