import pygame

pygame.init()
run = True
# window setup
win = pygame.display.set_mode((500, 500))
screen_width = 500
# window name
pygame.display.set_caption("Practice Game")
# characters location and values
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


x = 40
y = 400
width = 64
height = 64
velocity = 5

global enemyx
enemyx = 150
enemyy = 400
enemywidth = 64
enemyheight = 64
enemyvelocity = 3
path = [x, 500]
clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0
ewalkCount = 0


# enemy
enemyR = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
              pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
              pygame.image.load('R7E.png'), pygame.image.load('R8E.png')]
enemyL = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
              pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
              pygame.image.load('L7E.png'), pygame.image.load('L8E.png')]
enemyRattack = [pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
enemyLattack = [pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]



def gameWindow():
    global enemyx
    global walkCount
    global ewalkCount
    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

   #enemy movement
    if ewalkCount + 1 >= 16:
        ewalkCount = 0
    if enemyx < path[1]+enemyvelocity and enemyx != 200:
        if x < enemyx and x - 20 != enemyx:
            enemyx -= enemyvelocity
           # print(enemyx, x)
            win.blit(enemyL[ewalkCount // 4], (enemyx, enemyy))
            ewalkCount += 1
    if enemyx < path[1]+enemyvelocity and enemyx != 200:
        if x > enemyx and x + 20 != enemyx:
            enemyx += enemyvelocity
           # print(enemyx, x)
            win.blit(enemyR[ewalkCount // 4], (enemyx, enemyy))
            ewalkCount += 1

        elif enemyx == x -20:
            #win.blit(enemyLattack)
            print("blam")

        elif enemyx == x + 20:
            #win.blit(enemyRattack)
            print("blam")


    pygame.display.update()




while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # inputs to move character
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - velocity:
        x += velocity
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0

    if not (isJump):
        if keys[pygame.K_UP]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    gameWindow()
pygame.quit()
