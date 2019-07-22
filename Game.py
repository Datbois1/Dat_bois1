import pygame
pygame.init
Screensize = (width, height) = (800,600)
screen = pygame.display.set_mode(Screensize)
clock = pygame.time.Clock()
color = (155, 44, 88)
screen.fill(color)
pygame.display.flip()