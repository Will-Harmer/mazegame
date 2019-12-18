import random, savehelper, pygame
from savehelper import *
complete = True
def createmaze():
    complete = False
    playerx = int(loadvar("playerx"))
    playery = int(loadvar("playery"))
    flagx = int(loadvar("flagx"))
    flagy = int(loadvar("flagy"))
    bomb1x = int(loadvar("bomb1x"))
    bomb1y = int(loadvar("bomb1y"))
    bomb2x = int(loadvar("bomb2x"))
    bomb2y = int(loadvar("bomb2y"))
    score = int(loadvar("score"))
    complete =bool(loadvar("complete"))
    flagx = random.randint(0,800)
    flagy = random.randint(0,600)
    bomb1x = random.randint(0, 800)
    bomb1y = random.randint(0, 600)
    bomb2x = random.randint(0, 800)
    bomb2y = random.randint(0, 600)
    flag = pygame.Rect(flagx, flagy, 50, 50)
    bomb1 = pygame.Rect(bomb1x, bomb1y, 50, 50)
    bomb2 = pygame.Rect(bomb2x, bomb2y, 50, 50)
    player=pygame.Rect(playery,playerx,50,50)
    while flag.colliderect(bomb1) or player.colliderect(bomb1):
        bomb1x = random.randint(0, 800)
        bomb1y = random.randint(0, 600)
    while flag.colliderect(bomb2) or player.colliderect(bomb2):
        bomb2x = random.randint(0, 800)
        bomb2y = random.randint(0, 600)
    print("one point gained")
    save(playerx,"playerx")
    save(playery,"playery")
    save(flagx,"flagx")
    save(flagy,"flagy")
    save(bomb1x, "bomb1x")
    save(bomb1y, "bomb1y")
    save(bomb2x, "bomb2x")
    save(bomb2y, "bomb2y")
    save(score, "score")
    save(complete,"complete")
    saveall()