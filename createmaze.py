import random, savehelper, pygame
from savehelper import *
complete = True

def createmaze(size):
    complete = False
    playerx = int(loadvar("playerx"))
    playery = int(loadvar("playery"))
    flagx = int(loadvar("flagx"))
    flagy = int(loadvar("flagy"))
    score = int(loadvar("score"))
    bombs = loadlist("bombs")
    complete =bool(loadvar("complete"))
    numberofbombs = round(score/25)+1
    if score <= 0:
        numberofbombs = 0
    flagx = random.randint(0,size[0]-50)
    flagy = random.randint(0,size[1]-50)
    bombs = []
    flag = pygame.Rect(flagx, flagy, 50, 50)
    player=pygame.Rect(playery,playerx,50,50)
    for lmao in range(numberofbombs):
        tempbombx = random.randint(0, size[0]-50)
        tempbomby = random.randint(0, size[1]-50)
        tempbomb = pygame.Rect(tempbombx, tempbomby, 50, 50)
        while flag.colliderect(tempbomb) or player.colliderect(tempbomb):
            tempbombx = random.randint(0, size[0]-50)
            tempbomby = random.randint(0, size[1]-50)
            tempbomb = pygame.Rect(tempbombx, tempbomby, 50, 50)
        bomb11 = tempbombx
        bomb22 = tempbomby
        bombs.append(bomb11)
        bombs.append(bomb22)

    save(playerx,"playerx")
    save(playery,"playery")
    save(flagx,"flagx")
    save(flagy,"flagy")
    save(bombs, "bombs")
    save(score, "score")
    save(complete,"complete")
    saveall()
