import pygame
pygame.init()
#window setup
win = pygame.display.set_mode((500, 480))
screen_width = 500
#window name
pygame.display.set_caption("Practice Game")
#charachters location and values
walkRight = [pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R1.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R2.png'),
             pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R3.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R4.png'),
             pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R5.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R6.png'),
             pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R7.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R8.png'),
             pygame.image.load(r'C:\Users\Riley\Downloads\sprites\R9.png')]
walkLeft = [pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L1.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L2.png'),
            pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L3.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L4.png'),
            pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L5.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L6.png'),
            pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L7.png'), pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L8.png'),
            pygame.image.load(r'C:\Users\Riley\Downloads\sprites\L9.png')]
bg = pygame.image.load(r'C:\Users\Riley\Downloads\sprites\dun.jpg')
char = pygame.image.load(r'C:\Users\Riley\Downloads\sprites\standing.png')


x = 50
y = 400
width = 64
height = 64
velocity = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def gameWindow():
    global walkCount

    win.blit(bg, (0, 0))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#inputs to move character
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_width - width - velocity :
        x += velocity
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
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
#Zackery Dean

