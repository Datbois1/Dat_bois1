import pygame
from bullet import *
pygame.init()
Screensize = (width, height) = (800,600)
screen = pygame.display.set_mode(Screensize)
color = (165, 42, 42)
clock = pygame.time.Clock()
screeninfo = pygame.display.Info()
bullet = bullet()


def main():
    while True:
        clock.tick(60)
        bullet.Move()
        screen.fill(color)
        bullet.draw(screen)
        pygame.display.flip()


if __name__== "__main__":
    main()

