import pygame
import random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((900, 900), pygame.RESIZABLE)
pygame.display.set_caption("Sierpinski's triangle via chaos game")

black = (0, 0, 0)
white = (255, 255, 255)


def find_midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y


def draw_pixel_from_buffer(buffer):
    for element in buffer:
        pygame.draw.line(screen, white, [x, y], [x, y + 1], 1)
    pygame.display.flip()
    return


def make_buffer(size_x, size_y):
    buffer = []

    for row in range(size_y):
        r = []
        for column in range(size_x):
            r.append(0)
        buffer.append(r)
    return buffer


while True:
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    x = 500
    y = 500

    buffer = make_buffer(x, y)

    for i in range(10000):
        n = random.randint(1, 3)
        if n == 1:
            x, y = find_midpoint(x, y, 500, 100)
        elif n == 2:
            x, y = find_midpoint(x, y, 200, 500)
        elif n == 3:
            x, y = find_midpoint(x, y, 800, 500)

        draw_pixel_from_buffer(buffer)
        clock.tick(8)
