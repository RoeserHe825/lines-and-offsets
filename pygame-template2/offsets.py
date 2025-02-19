# loops and offsets
# Henry Roeser
# 2/19/25

import pygame
import sys
import config


pygame.init()
screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constans from config
pygame.display.set_caption(config.TITLE)
# Draw on the screen multiple lines starting from (0, 10) to (100, 110)
# Each line will have a width of 5 pixels

y_offset = 0
thickness = 5
while y_offset < 100:
    pygame.draw.line(screen, config.RED, [0, 10 + y_offset], [100, 110 + y_offset], thickness)
    y_offset = y_offset + 10


x_offset = 10
thickness = 7
while x_offset < 100:
    pygame.draw.line(screen, config.BLUE, [30, 30 + x_offset], [90, 80 + x_offset], thickness)
    x_offset = x_offset + 10
pygame.display.flip()

running = True # Keep window up 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # Quit Pygame
sys.exit() # Exit the program