import pygame, sys

pygame.init()

gameExit = False
gameDisplay = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
FPS = 60

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
#The code below draws out the coloured objects for the game
whiteSquare = pygame.draw.rect(gameDisplay, white, [100, 150, 30, 30])
redSquare = pygame.draw.rect(gameDisplay, red, [150, 100, 20, 20])
blueSquare = pygame.draw.rect(gameDisplay, blue, [100, 200, 40, 40])
yellowSquare = pygame.draw.rect(gameDisplay, yellow, [200, 100, 50, 50])
greenSquare = pygame.draw.rect(gameDisplay, green, [100, 200, 10, 10])

#The following coding adds or subtracts point from the object
#Depending on the colour it has selected
def reward(points):
    if pygame.Rect.colliderect(whiteSquare, greenSquare) or pygame.Rect.colliderect(whiteSquare, blueSquare) or pygame.Rect.colliderect(whiteSquare, yellowSquare):
        points += 1
    if pygame.Rect.colliderect(whiteSquare, redSquare):
        points -= 1
    return points


points = 0
#allows the user to control the white square
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                whiteSquare.centery -= 5
            if event.key == pygame.K_DOWN:
                whiteSquare.centery += 5
            if event.key == pygame.K_LEFT:
                whiteSquare.centerx -= 5
            if event.key == pygame.K_RIGHT:
                whiteSquare.centerx += 5


    gameDisplay.fill(black)
    redSquare = pygame.draw.rect(gameDisplay, red, [150, 100, 20, 20])
    blueSquare = pygame.draw.rect(gameDisplay, blue, [100, 200, 40, 40])
    yellowSquare = pygame.draw.rect(gameDisplay, yellow, [200, 100, 50, 50])
    greenSquare = pygame.draw.rect(gameDisplay, green, [100, 200, 10, 10])

    #collision detections
    #allows the object to take on different colours
    if pygame.Rect.colliderect(whiteSquare, greenSquare):
        pygame.draw.rect(gameDisplay, green, whiteSquare)
    elif pygame.Rect.colliderect (whiteSquare, blueSquare):
        pygame.draw.rect(gameDisplay, blue, whiteSquare)
    elif pygame.Rect.colliderect (whiteSquare, yellowSquare):
        pygame.draw.rect(gameDisplay, yellow, whiteSquare)
    elif pygame.Rect.colliderect (whiteSquare, redSquare):
        pygame.draw.rect(gameDisplay, red, whiteSquare)
    else:
        pygame.draw.rect(gameDisplay, white, whiteSquare)

    points = reward(points)
    
    print(points)
        
    pygame.display.update()

    clock.tick(FPS)
    pygame.display.update()
