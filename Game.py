import pygame
pygame.init
Screensize = (width, height) = (800,600)
screen = pygame.display.set_mode(Screensize)
color = (165, 42, 42)
clock = pygame.time.Clock()
Bullet = pygame.image.load("bullet.png")
Bullet = pygame.transform.scale(Bullet, (100, 50))
bullet_rect = Bullet.get_rect()
speed = pygame.math.Vector2(10, 10)
screeninfo = pygame.display.Info()
def main():
    while True:
        clock.tick(60)
        Move()
        screen.fill(color)
        screen.blit(Bullet, bullet_rect)
        pygame.display.flip()
def Move():
    bullet_rect.move_ip(speed)
    width = screeninfo.current_w
    if bullet_rect.right > width:
        speed.x *= -1
    if bullet_rect.left < 0:
        speed.x  *=-1
    if bullet_rect.top < height:
        speed.y *=-1
    if bullet_rect.bottom > 0:
        speed.y *=-1




if __name__=="__main__":
    main()

