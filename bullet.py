class bullet:
    def __init__(self, pos):
    self.image = pygame.image.load("bullet.png")
    self.image = pygame.transform.scale(self.image, (100, 50))
    self.rect = Bullet.get_rect()
    self.speed = pygame.math.Vector2(10, 10)