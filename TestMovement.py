import pygame
pygame.init()
#window setup
win = pygame.display.set_mode((600,600))
screen_width = 600
#window name
pygame.display.set_caption("Practice Game")
#charachters location and values
x = 10
y = 10
width = 10
height = 10
velocity = 3

isJump = False
jumpCount = 5
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False
#inputs to move character
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT or pygame.K_a] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT or pygame.K_d] and x < screen_width - width - velocity :
        x += velocity
    if not (isJump):
        if keys[pygame.K_UP or pygame.K_w] and y > velocity :
            y -= velocity
        if keys[pygame.K_DOWN or pygame.K_s] and y < screen_width - height - velocity:
            y += velocity
        if keys[pygame.K_SPACE] and y > velocity:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()


pygame.quit()