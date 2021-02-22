def enemyWindow():
    global enemyx
    global ewalkCount
   #enemy movement
    if ewalkCount + 1 >= 16:
        ewalkCount = 0
    if enemyx < path[1]+enemyvelocity and enemyx != 200:
        if x < enemyx and x != enemyx:
            enemyx -= enemyvelocity
           # print(enemyx, x)
            win.blit(enemyL[ewalkCount // 4], (enemyx, enemyy))
            ewalkCount += 1
    if enemyx < path[1]+enemyvelocity and enemyx != 200:
        if x > enemyx and x != enemyx:
            enemyx += enemyvelocity
           # print(enemyx, x)
            win.blit(enemyR[ewalkCount // 4], (enemyx, enemyy))
            ewalkCount += 1

    if enemyx -1 == x and enemyy == y:
        #win.blit(enemyLattack//ewalkCount // 4)
        print("blam")

    if enemyx + 1 == x and enemyy == y:
        #win.blit(enemyRattack)
        print("blamo")
    if enemyx == x and enemyy == y:
        print("You have died")

    pygame.display.update()