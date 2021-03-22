import pygame
import time

pygame.init()
run = True
# window setup
win = pygame.display.set_mode((500, 500))
screen_width = 500
# window name
pygame.display.set_caption("Enemy Testing Grounds")
clock = pygame.time.Clock()
walkCount = 0

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


class player(object):
    # characters location and values
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.vel = 3
        self.isJump = False
        self.left = False
        self.right = False
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.y > 410:
            self.y = 410
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    def hit(self):
        self.y = 410
        self.x = 60
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 30)
        text = font1.render('Hit', 1, (100, 22, 117))
        win.blit(text, (self.x, self.y+10))
        pygame.display.update()
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
#enemyclass
class enemy(object):
    enemyR = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
              pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
              pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]
    enemyL = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
              pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
              pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]
    enemyRattack = [pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    enemyLattack = [pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, startx, y, width, height, end, isalive):
        self.alive = isalive
        self.start = startx
        self.x = startx
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.start, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.tod = 0



    def draw(self, win):
        if self.alive == True:
            self.move()

            if self.walkCount >= 16:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.enemyR[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.enemyL[self.walkCount // 4], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            pygame.draw.rect(win, (100, 22, 117), self.hitbox, 2)
        else:
            self.hitbox = (0,0,0,0)


    def move(self):
        self.x += self.vel
        if self.x < self.start:
            self.x = self.start
            self.walkCount = 0
        if self.x > self.end:
            self.x = self.end
            self.walkCount = 0
        if man.x >= self.path[0] and man.x <= self.path[1]:
            if man.x <= self.x and man.y == self.y:
                print("moving left")
                if self.vel > 0:
                    self.vel = self.vel * -1

            elif man.x >= self.x and man.y == self.y:
                print("moving right")
                if self.vel < 0:
                    self.vel = self.vel * -1

        else:
            self.walkPath()
    def walkPath(self):
        print("Patroling")
        if self.x >= self.path[1]:
            self.vel = self.vel * -1
            self.walkCount = 0
        elif self.x == self.path[0]:
            self.vel = self.vel*-1
            self.walkCount = 0
    def attack(self):
        if man.x < self.x:
            win.blit(self.enemyL[self.walkCount // 4], (self.x, self.y))
        else:
            win.blit(self.enemyRattack[self.walkCount // 4], (self.x, self.y))
    def hit(self):
        print("Hit")
        self.alive = False
        self.ressurect()
    def ressurect(self):
        print("Begining Necromancy")
        self.currentTime = pygame.time.get_ticks()
        self.passedTime = self.currentTime - self.tod
        print(self.tod)
        print(self.passedTime)
        print(self.currentTime)
        if(self.passedTime >= self.tod+5000):
            print(self.passedTime)
            print("He is reborn")
            self.alive = True
class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


# mainloop
man = player(200, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450, True)
shootLoop = 0
bullets = []
run = True
while run:
    clock.tick(27)
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            # goblin.attack()
            man.hit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + \
                    goblin.hitbox[2]:
                goblin.hit()
                goblin.tod = pygame.time.get_ticks()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

        shootLoop = 1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
    redrawGameWindow()

pygame.quit()
