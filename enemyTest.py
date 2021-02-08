import pygame  
pygame.init()

pygame.display.set_caption("enemy test")


class enemy(object):
    enemyR = [pygame.image.load('R1E.png'),pygame.image.load('R2E.png'),pygame.image.load('R3E.png'),pygame.image.load('R4E.png'),pygame.image.load('R5E.png'),pygame.image.load('R6E.png'),pygame.image.load('R7E.png'),pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]
    enemyL = [pygame.image.load('L1E.png'),pygame.image.load('L2E.png'),pygame.image.load('L3E.png'),pygame.image.load('L4E.png'),pygame.image.load('L5E.png'),pygame.image.load('L6E.png'),pygame.image.load('L7E.png'),pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]
    enemyRattack = [pygame.image.load('R10E.png'),pygame.image.load('R11E.png')]
    enemyLattack = [pygame.image.load('L10E.png'),pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3

goblin = enemy(100, 410, 64, 64, 300)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    redrawGameWindow()

pygame.quit()