import pygame


class bullet:
    def __init__(self):
        self.image = pygame.image.load("bullet.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.speed = pygame.math.Vector2(10, 10)


    def Move(self):
        screeninfo = pygame.display.Info()
        self.rect.move_ip(self.speed)
        width = screeninfo.current_w
        height = screeninfo.current_h
        if self.rect.right > width:
            self.speed.x *= -1
        if self.rect.left < 0:
            self.speed.x *= -1
        if self.rect.top < height:
            self.speed.y *= -1
        if self.rect.bottom > 0:
            self.speed.y *= -1
    def draw(self, screen):
        screen.blit(self.image, self.rect)
