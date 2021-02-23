import pygame

pygame.init()
run = True
# window setup
win = pygame.display.set_mode((500, 500))
screen_width = 500
# window name
pygame.display.set_caption("Enemy and Player")
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
        print('hit')
        self.y = 410
        self.x = 60
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 30)
        text = font1.render('Hit', 1, (255, 0, 0))
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

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
    def draw(self, win):
        self.move()
        if self.walkCount >= 16:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.enemyR[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
            #print(self.x, self.vel, self.walkCount)
        else:
            win.blit(self.enemyL[self.walkCount // 4], (self.x, self.y))
            self.walkCount += 1
            #print(self.x, self.vel, self.walkCount)
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        self.x += self.vel
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


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)

    pygame.display.update()


# mainloop
man = player(60, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 300)
run = True
while run:
    clock.tick(27)
    if man.hitbox[1] < goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+ man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                #goblin.attack()
                man.hit()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

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
