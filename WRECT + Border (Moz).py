import random, time, sys, pygame, border #REFERENCE: here we use the Pygame Library developed by ____ and published by ___

from pygame.locals import *
pygame.init() 

#coordinates for the different values of the RectsValues variable
Xpos  = 65
Ypos  = 35

Xpos1 = 65
Ypos1 = 145

Xpos2 = 65
Ypos2 = 235

Xpos3 = 65
Ypos3 = 335

Xpos4 = 65
Ypos4 = 435

#setting up the
#colours    R    G    B
black     = ( 30,  30,  30) 
white     = (192, 192, 192) 
green     = ( 32, 178, 170)
blue      = ( 50, 120, 220)
yellow    = (255, 215,   0)
red       = (255,  69,   0)
lavender  = (230, 230, 250)
honeydrew = (240, 255, 240) #This color is used only for the PRESS SPACE FOR THE GAME TO BEGIN screen message

#setting up the game window
displayHeight = 500
displayWidth  = 800
displaySurface = pygame.display.set_mode((displayWidth, displayHeight), pygame.RESIZABLE)
pygame.display.set_caption('WRECT.io')

#different fonts to use
fontType  = pygame.font.SysFont("genevasansserif", 50)
fontType2 = pygame.font.SysFont("genevasansserif", 25)
fontType3 = pygame.font.SysFont("genevasansserif", 20)

#assigning colours to different variables for easier use 
ObjectsColour  = white
RectsColour    = green
STARTcolour    = blue
shape1colour   = white
shape2colour   = white
shape3colour   = green
shape4colour   = green

#other variables
Pointer         = 'Option1' #_______________________
ObjectsValue    = 1
RectsValue      = 1
 
#Reference: Learned how to do that function in one of the videos of TheNewBoston
def text_objects(text, color, FontName):
    textSurface = FontName.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Function to show a message to the screen
def text_to_screen(text, color, FontName, pos):
    textSurf, textRect = text_objects(text, color, FontName)
    textRect.center = ((displayWidth / 2)), (pos)
    displaySurface.blit(textSurf, textRect)

#Intro/Menu function 
def Menu(): 
    #____________
    global Pointer, ObjectsColour, ObjectsValue, RectsColour, RectsValue, STARTcolour, startGame, shape1colour, shape2colour, shape3colour, shape4colour

    Menu = True

    #the Menu loop will run untill ENTER (RETURN) is pressed and will then call the Game function which is basically the game itself
    while Menu: 
        
        #Graphics that make the Menu
        displaySurface.fill(black)
        shape1 = pygame.draw.rect(displaySurface, shape1colour, (468, 199, 6, 6))
        shape2 = pygame.draw.rect(displaySurface, shape2colour, (498, 199, 6, 6))
        shape3 = pygame.draw.rect(displaySurface, shape3colour, (459, 259, 6, 6))
        shape4 = pygame.draw.rect(displaySurface, shape4colour, (491, 259, 6, 6))
        pygame.draw.line(displaySurface, blue, (30,  102), (205, 102), 2)
        pygame.draw.line(displaySurface, blue, (597, 102), (771, 102), 2)
        text_to_screen('Objects:   ' + str(ObjectsValue), ObjectsColour,  fontType, 200) 
        text_to_screen('Rects:     ' + str(RectsValue),     RectsColour,  fontType, 260)
        text_to_screen('Welcome to WRECT',                         blue,  fontType, 100)
        text_to_screen('PRESS ENTER TO START GAME',         STARTcolour, fontType2, 370) 
        text_to_screen('ESC TO CLOSE THE GAME',             STARTcolour, fontType3, 415)

        #This part makes the last two messages to the screen blink
        if STARTcolour == blue:
            STARTcolour = black
            time.sleep(0.15)
        elif STARTcolour == black:
            STARTcolour   = blue
            time.sleep(0.15)

        pygame.display.update()
       

        #Event handling for navigating through the menu
        for event in pygame.event.get():
            print(event)  ## TO REMOVE after tests are done
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if Pointer == 'Option1':
                        ObjectsColour = green
                        shape1colour  = green
                        shape2colour  = green
                        shape3colour  = white

                        shape4colour  = white
                        RectsColour   = white
                        Pointer       = 'Option2'
                if event.key == pygame.K_UP:
                    if Pointer == 'Option2':
                        ObjectsColour = white
                        shape1colour  = white
                        shape2colour  = white
                        shape3colour  = green
                        shape4colour  = green
                        RectsColour   = green                        
                        Pointer       = 'Option1'
                if event.key == pygame.K_RIGHT:
                    if Pointer == 'Option1':
                        if ObjectsValue < 5:
                            ObjectsValue += 1
                    if Pointer == 'Option2':
                        if RectsValue < 5:
                            RectsValue += 1
                    ######  ObjectsValue = RectsValue * 2 do later
                if event.key == pygame.K_LEFT:
                    if Pointer == 'Option1':
                        if ObjectsValue > 1:
                            ObjectsValue -= 1
                    if Pointer == 'Option2':
                        if RectsValue > 1:
                            RectsValue -= 1
                            
                # If RETURN pressed Game() function is called and the game itself starts  
                if event.key == pygame.K_RETURN:
                    Menu = False
                    Game()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

#Main Game function, aka where the **MAGIC** happens
def Game():  
    while Game:
        border.Run(RectsValue)

Menu()
