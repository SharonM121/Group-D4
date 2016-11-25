import pygame, sys
from pygame.locals import *
import random
def RandomRectangle(screenSize, amount):
    coords = []
    screenWidth = screenSize[0] - 100
    screenHeight = screenSize[1] - 100

    for i in range(amount):
        coords.append((random.randint(100, screenWidth), random.randint(100, screenHeight)))
    print(coords)
    return coords

def DrawObstacles(coords, screen):
    for i in range(0, len(coords)):
        pygame.draw.rect(screen,(255,255,255), (coords[i][0], coords[i][1], 50, 50))

def Run(amount):
    pygame.init()
    screen = pygame.display.set_mode((500,500), pygame.RESIZABLE)
    coordinates = RandomRectangle((screen.get_width(),screen.get_height()), amount)
    pygame.display.set_caption("SNEK")

    pygame.display.flip()

    gameExit = False
    while not gameExit:

        pygame.event.pump()
        width = screen.get_width() - 50
        height = screen.get_height() - 50
        centerx = screen.get_width()/2
        centery = screen.get_height()/2
        rect = pygame.draw.rect(screen, (255, 0, 0), (centerx - (width/2), centery - (height/2), width, height))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'],RESIZABLE)
                pygame.display.flip()
        DrawObstacles(coordinates, screen)
        pygame.display.update()
    myfont = pygame.font.SysFont("ariel", 18)
    clock=pygame.time.Clock()

    score = 0
    scoretext = myfont.render("Score: {0}".format(score), 1, (white))
    screen.blit(scoretext, (50, 50))
    score += 1

    white = (255, 255, 255)

    message = 'your message'
    font = pygame.font.Font(None, 40)
    text = font.render(message, 1, white)
    screen.blit(text, (x_position,y_position),rect)
    pygame.display.update()

    pygame.quit()
    quit()
