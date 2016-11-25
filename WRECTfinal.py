import random, time, sys, pygame #REFERENCE: here we use the Pygame Library developed by the Pygame Community.
                                 #It's original author is Pete Shinners and was released
                                 #Released on the 28th of October 2000

from pygame.locals import * # Imports all the available pygame modules into the pygame package

pygame.init() 

#fixed starting point coordinates for the different values of the RectsValues variable
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
honeydrew = (240, 255, 240) #This colour is used only for the "PRESS SPACE FOR THE GAME TO BEGIN" screen message

#setting up the game window
displayHeight = 500
displayWidth  = 800
displaySurface = pygame.display.set_mode((displayWidth, displayHeight))
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
    global Pointer, ObjectsColour, ObjectsValue, RectsColour, RectsValue, STARTcolour, shape1colour, shape2colour, shape3colour, shape4colour

    Menu = True

    #The Menu loop will run untill ENTER (RETURN) is pressed and will then call the Game function which is basically the game itself
    while Menu: 
        
        #Graphics that make the Menu
        displaySurface.fill(black)
        shape1 = pygame.draw.rect(displaySurface, shape1colour, (461, 199, 6, 6))
        shape2 = pygame.draw.rect(displaySurface, shape2colour, (508, 199, 6, 6))
        shape3 = pygame.draw.rect(displaySurface, shape3colour, (461, 259, 6, 6))
        shape4 = pygame.draw.rect(displaySurface, shape4colour, (508, 259, 6, 6))
        pygame.draw.line(displaySurface, blue, (30,  102), (205, 102), 2)
        pygame.draw.line(displaySurface, blue, (597, 102), (771, 102), 2)
        text_to_screen('Objects:   ' + str(ObjectsValue),   ObjectsColour,  fontType, 200) 
        text_to_screen('Rects:       ' + str(RectsValue),     RectsColour,  fontType, 260)
        text_to_screen('Welcome to WRECT',                           blue,  fontType, 100)
        text_to_screen('PRESS ENTER TO START THE GAME',       STARTcolour, fontType2, 370) 
        text_to_screen('ESC TO CLOSE THE GAME',               STARTcolour, fontType3, 415)

        #This part makes the last two text messages on the screen blink
        if STARTcolour == blue:
            STARTcolour = black
            time.sleep(0.15)
        elif STARTcolour == black:
            STARTcolour   = blue
            time.sleep(0.15)

        pygame.display.update()
       

        #Events in the Menu 
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
                        if ObjectsValue < 10:
                            ObjectsValue += 1
                    if Pointer == 'Option2':
                        if RectsValue < 5:
                            RectsValue += 1
                            ObjectsValue = RectsValue * 2
                            
                if event.key == pygame.K_LEFT:
                    if Pointer == 'Option1':
                        if ObjectsValue > 1:
                            ObjectsValue -= 1
                    if Pointer == 'Option2':
                        if RectsValue > 1:
                            RectsValue -= 1
                            ObjectsValue = RectsValue * 2
                            
                # If ENTER is pressed, the Game() function is called and the game screen appears  
                if event.key == pygame.K_RETURN:
                    Menu = False
                    Game()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


#Main Game function, aka where the **MAGIC** happens
def Game():  
    #_______________
    global Xno, Yno, Xno1, Yno1, Xno2, Yno2, Xno3, Yno3, Xno4, Yno4, Ypos, Xpos, Ypos1, Xpos1, Ypos2, Xpos2, Ypos3, Xpos3, Ypos4, Xpos4, honeydrew, rectObColour, blue, green, red, yellow, Xob, Yob, Xob1, Yob1, Xob2, Yob2, Xob3, Yob3, Xob4, Yob4

    Game = True
    Bool = False

    #Random coordinates generation for the Objects rectangles
    Xob  = random.randint(50,780)
    Yob  = random.randint(50,480)
    Xob1 = random.randint(50,780)
    Yob1 = random.randint(50,480)
    Xob2 = random.randint(50,780)
    Yob2 = random.randint(50,480)
    Xob3 = random.randint(50,780)
    Yob3 = random.randint(50,480)
    Xob4 = random.randint(50,780)
    Yob4 = random.randint(50,480)
    Xob5 = random.randint(50,780)
    Yob5 = random.randint(50,480)
    Xob6 = random.randint(50,780)
    Yob6 = random.randint(50,480)
    Xob7 = random.randint(50,780)
    Yob7 = random.randint(50,480)
    Xob8 = random.randint(50,780)
    Yob8 = random.randint(50,480)
    Xob9 = random.randint(50,780)
    Yob9 = random.randint(50,480)
    
    #Random coordinates generation for the RED(Don't touch) rectangles
    Xno  = random.randint(50,780)
    Yno  = random.randint(50,480)
    Xno1 = random.randint(50,780)
    Yno1 = random.randint(50,480)
    Xno2 = random.randint(50,780)
    Yno2 = random.randint(50,480)
    Xno3 = random.randint(50,780)
    Yno3 = random.randint(50,480)
    Xno4 = random.randint(50,780)
    Yno4 = random.randint(50,480)
    Xno5 = random.randint(50,780)
    Yno5 = random.randint(50,480)
    Xno6 = random.randint(50,780)
    Yno6 = random.randint(50,480)
    Xno7 = random.randint(50,780)
    Yno7 = random.randint(50,480)
    Xno8 = random.randint(50,780)
    Yno8 = random.randint(50,480)
    Xno9 = random.randint(50,780)
    Yno9 = random.randint(50,480)
    
    #Frames Per Second, or how fast the objects will move
    clock = pygame.time.Clock()

    colourList    = [blue, yellow, green]
    rectObColour  = random.choice(colourList)
    rectObColour1 = random.choice(colourList)
    rectObColour2 = random.choice(colourList)
    rectObColour3 = random.choice(colourList)
    rectObColour4 = random.choice(colourList)


    #main game loop **(handles events, updates the game state, draws the game state to the screen)**
    while Game: 

        
        displaySurface.fill(white)
        #BORDER, MOZAMEL'S CODE SHOULD BE HERE



        

        #Text for the actual start of the game
        text_to_screen('PRESS SPACE FOR THE GAME TO BEGIN', honeydrew, fontType2, 250)

        #Drawing the RED(Don't touch) rectangles and increasing the speed depending on the value of RectsValue
        if RectsValue == 1:
            noTouchRect  = pygame.draw.rect(displaySurface, red, [Xno,   Yno, 20, 20])
            noTouchRect1 = pygame.draw.rect(displaySurface, red,[Xno1,  Yno1, 20, 20])
            FPS = 10 ##
        elif RectsValue == 2:
            noTouchRect  = pygame.draw.rect(displaySurface, red, [Xno,   Yno, 20, 20])
            noTouchRect1 = pygame.draw.rect(displaySurface, red,[Xno1,  Yno1, 20, 20])
            noTouchRect2 = pygame.draw.rect(displaySurface, red,[Xno2,  Yno2, 20, 20])
            noTouchRect3 = pygame.draw.rect(displaySurface, red,[Xno3,  Yno3, 20, 20])
            FPS = 13 ##
        elif RectsValue == 3:
            noTouchRect  = pygame.draw.rect(displaySurface, red, [Xno,   Yno, 20, 20])
            noTouchRect1 = pygame.draw.rect(displaySurface, red,[Xno1,  Yno1, 20, 20])
            noTouchRect2 = pygame.draw.rect(displaySurface, red,[Xno2,  Yno2, 20, 20])
            noTouchRect3 = pygame.draw.rect(displaySurface, red,[Xno3,  Yno3, 20, 20])
            noTouchRect4 = pygame.draw.rect(displaySurface, red,[Xno4,  Yno4, 20, 20])
            noTouchRect5 = pygame.draw.rect(displaySurface, red,[Xno5,  Yno5, 20, 20])
            FPS = 16 ##
        elif RectsValue == 4:
            noTouchRect  = pygame.draw.rect(displaySurface, red, [Xno,   Yno, 20, 20])
            noTouchRect1 = pygame.draw.rect(displaySurface, red,[Xno1,  Yno1, 20, 20])
            noTouchRect2 = pygame.draw.rect(displaySurface, red,[Xno2,  Yno2, 20, 20])
            noTouchRect3 = pygame.draw.rect(displaySurface, red,[Xno3,  Yno3, 20, 20])
            noTouchRect4 = pygame.draw.rect(displaySurface, red,[Xno4,  Yno4, 20, 20])
            noTouchRect5 = pygame.draw.rect(displaySurface, red,[Xno5,  Yno5, 20, 20])
            noTouchRect6 = pygame.draw.rect(displaySurface, red,[Xno6,  Yno6, 20, 20])
            noTouchRect7 = pygame.draw.rect(displaySurface, red,[Xno7,  Yno7, 20, 20])
            FPS = 19 ##
        elif RectsValue == 5:
            noTouchRect  = pygame.draw.rect(displaySurface, red, [Xno,   Yno, 20, 20])
            noTouchRect1 = pygame.draw.rect(displaySurface, red,[Xno1,  Yno1, 20, 20])
            noTouchRect2 = pygame.draw.rect(displaySurface, red,[Xno2,  Yno2, 20, 20])
            noTouchRect3 = pygame.draw.rect(displaySurface, red,[Xno3,  Yno3, 20, 20])
            noTouchRect4 = pygame.draw.rect(displaySurface, red,[Xno4,  Yno4, 20, 20])
            noTouchRect5 = pygame.draw.rect(displaySurface, red,[Xno5,  Yno5, 20, 20])
            noTouchRect6 = pygame.draw.rect(displaySurface, red,[Xno6,  Yno6, 20, 20])
            noTouchRect7 = pygame.draw.rect(displaySurface, red,[Xno7,  Yno7, 20, 20])
            noTouchRect8 = pygame.draw.rect(displaySurface, red,[Xno8,  Yno8, 20, 20])
            noTouchRect9 = pygame.draw.rect(displaySurface, red,[Xno9,  Yno9, 20, 20])
            FPS = 21 ##
            

        #Drawing the different rectangles that will be collecting other rectangles depending on the
        #given value in the Menu
        if RectsValue == 1:
            rect1 = pygame.draw.rect(displaySurface, lavender, [Xpos,  Ypos, 20, 20])
        elif RectsValue == 2:
            rect1 = pygame.draw.rect(displaySurface, lavender, [Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
        elif RectsValue == 3:
            rect1 = pygame.draw.rect(displaySurface, lavender, [Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
        elif RectsValue == 4:
            rect1 = pygame.draw.rect(displaySurface, lavender ,[Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
            rect4 = pygame.draw.rect(displaySurface, lavender,[Xpos3, Ypos3, 20, 20])
        elif RectsValue == 5:
            rect1 = pygame.draw.rect(displaySurface, lavender, [Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
            rect4 = pygame.draw.rect(displaySurface, lavender,[Xpos3, Ypos3, 20, 20])
            rect5 = pygame.draw.rect(displaySurface, lavender,[Xpos4, Ypos4, 20, 20])


        #Drawing the Objects rectangles and generating random coordinates and random colours for them
        if ObjectsValue == 1:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,  Yob, 20, 20])
        elif ObjectsValue == 2:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,  Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour2,[Xob1, Yob1, 20, 20])
        elif ObjectsValue == 3:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,  Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour2,[Xob1, Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour3,[Xob2, Yob2, 20, 20])
        elif ObjectsValue == 4:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
        elif ObjectsValue == 5:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
        elif ObjectsValue == 6:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
            rectOb5 = pygame.draw.rect(displaySurface, rectObColour4,[Xob5,  Yob5, 20, 20])
        elif ObjectsValue == 7:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
            rectOb5 = pygame.draw.rect(displaySurface, rectObColour4,[Xob5,  Yob5, 20, 20])
            rectOb6 = pygame.draw.rect(displaySurface, rectObColour4,[Xob6,  Yob6, 20, 20])
        elif ObjectsValue == 8:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
            rectOb5 = pygame.draw.rect(displaySurface, rectObColour4,[Xob5,  Yob5, 20, 20])
            rectOb6 = pygame.draw.rect(displaySurface, rectObColour4,[Xob6,  Yob6, 20, 20])
            rectOb7 = pygame.draw.rect(displaySurface, rectObColour4,[Xob7,  Yob7, 20, 20])
        elif ObjectsValue == 9:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour,  [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
            rectOb5 = pygame.draw.rect(displaySurface, rectObColour4,[Xob5,  Yob5, 20, 20])
            rectOb6 = pygame.draw.rect(displaySurface, rectObColour4,[Xob6,  Yob6, 20, 20])
            rectOb7 = pygame.draw.rect(displaySurface, rectObColour4,[Xob7,  Yob7, 20, 20])
            rectOb8 = pygame.draw.rect(displaySurface, rectObColour4,[Xob8,  Yob8, 20, 20])
        elif ObjectsValue == 10:
            rectOb  = pygame.draw.rect(displaySurface, rectObColour   [Xob,   Yob, 20, 20])
            rectOb1 = pygame.draw.rect(displaySurface, rectObColour1,[Xob1,  Yob1, 20, 20])
            rectOb2 = pygame.draw.rect(displaySurface, rectObColour2,[Xob2,  Yob2, 20, 20])
            rectOb3 = pygame.draw.rect(displaySurface, rectObColour3,[Xob3,  Yob3, 20, 20])
            rectOb4 = pygame.draw.rect(displaySurface, rectObColour4,[Xob4,  Yob4, 20, 20])
            rectOb5 = pygame.draw.rect(displaySurface, rectObColour4,[Xob5,  Yob5, 20, 20])
            rectOb6 = pygame.draw.rect(displaySurface, rectObColour4,[Xob6,  Yob6, 20, 20])
            rectOb7 = pygame.draw.rect(displaySurface, rectObColour4,[Xob7,  Yob7, 20, 20])
            rectOb8 = pygame.draw.rect(displaySurface, rectObColour4,[Xob8,  Yob8, 20, 20])
            rectOb9 = pygame.draw.rect(displaySurface, rectObColour4,[Xob9,  Yob9, 20, 20])
        
        ##MOVEMENT for the RECTS that will collect other rects (Should have been done by Muhammed, but he did not manage to do it on time
        #and I needed it, so I made it

        coordslist   = ['X', 'Y', 'Xneg', 'Yneg']
        coordsrandom = random.choice(coordslist)
        randcoords   = random.randint(4,10)
        randcoords1  = random.randint(4,10)
        randcoords2  = random.randint(4,10)
        randcoords3  = random.randint(4,10)
        randcoords4  = random.randint(4,10)

        if coordsrandom == coordslist[0] and Bool == True:
            Xpos  += randcoords+1
            Xpos1 += randcoords1+1
            Xpos2 += randcoords2+1
            Xpos3 += randcoords3+1
            Xpos4 += randcoords4+1
        elif coordsrandom == coordslist[1] and Bool == True:
            Ypos  += randcoords
            Ypos1 += randcoords1
            Ypos2 += randcoords2
            Ypos3 += randcoords3
            Ypos4 += randcoords4
            
        elif coordsrandom == coordslist[2] and Bool == True:
            Xpos  -= randcoords
            Xpos1 -= randcoords1
            Xpos2 -= randcoords2
            Xpos3 -= randcoords3
            Xpos4 -= randcoords4
            
        elif coordsrandom == coordslist[3] and Bool == True:
            Ypos  -= randcoords
            Ypos1 -= randcoords1
            Ypos2 -= randcoords2
            Ypos3 -= randcoords3
            Ypos4 -= randcoords4
        else:
            pass    

        #FPS and updating of the screen
        pygame.display.update()
        clock.tick(FPS)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()


            #If enter pressed, all drawn rectangles will move to some location
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    text_to_screen('PRESS SPACE FOR THE GAME TO BEGIN', white, fontType2, 250)
                    honeydrew = white
                    Bool = True
                if event.key == pygame.K_ESCAPE:
                    Game = False 
                    pygame.quit()
                    sys.exit
                    
                                      
            
Menu()
