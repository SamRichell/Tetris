import pygame
from matrix import Matrix
import tetrimino

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
dt = 0

matrix = Matrix(screen, 8, 20, 15)

matrix.summon_tetrimino(tetrimino.LShape())

count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    matrix.render()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    count += dt

    if count >= 0.75:

        count = 0
    