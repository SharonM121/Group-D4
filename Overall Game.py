import pygame, sys
#------------------ initialise the pygame engine --------------------
pygame.init()

#This sets the framework of the game - 800 width by 600 height
WIDTH = 800 #game window width
HEIGHT = 650 #game window height
framework = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 30 #the speed of the game, (frames per second) 
Pixsize = 20 #the size of the cell


#RGB values (colours)
WHITE = (255,255,255)
GREEN = (0,255,0)

#Note the term 'self' means, it can refer to the object itself
random = 0
class cell:
    def __init__(self): #It is used to initialise object instances
        self.x = random.randrange(10, WIDTH-10) #x position 
        self.y = random.randrange(10, HEIGHT-10) #y position 
        self.speed = random.randrange(2,15) #the speed of the cell 
        self.move = [None, None] #realtive x and y coordinates to move to
        self.direction = None #movement direction
        
#-------------- using compass coordinates for the objects to move randomly around the background ---------------------

    def draw(self):  
        pygame.draw.rect(framework, (GREEN), (self.x,self.y,Pixsize,Pixsize),0) #draw the cell

    def wander(self):
        directions = {"S":((-1,2),(1,self.speed)),"SW":((-self.speed,-1),(1,self.speed)),"W":((-self.speed,-1),(-1,2)),"NW":((-self.speed,-1),(-self.speed,-1)),"N":((-1,2),(-self.speed,-1)),"NE":((1,self.speed),(-self.speed,-1)),"E":((1,self.speed),(-1,2)),"SE":((1,self.speed),(1,self.speed))} #((min x, max x)(min y, max y))
        directionsName = ("S","SW","W","NW","N","NE","E","SE") #possible directions
        if random.randrange(0,10) == 2: #move about once every 10 frames
            if self.direction == None: #if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction) #get the index of direction in directions list
                b = random.randrange(a-1,a+2) #set the direction to be the same, or one next to the current direction
                if b > len(directionsName)-1: #if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]
            self.move[0] = random.randrange(directions[self.direction][0][0],directions[self.direction][0][1]) #change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0],directions[self.direction][1][1])  #change relative y to a random number between min y and max y
        if self.x < 5 or self.x > WIDTH - 5 or self.y < 5 or self.y > HEIGHT - 5: #if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > WIDTH - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > HEIGHT - 5:
                self.direction = "N"
            self.move[0] = random.randrange(directions[self.direction][0][0],directions[self.direction][0][1]) #change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0],directions[self.direction][1][1]) #change relative x to a random number between min x and max x
        if self.move[0] != None: #add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]
            
            
#This generates the number of cells which can be avaialble in the game
cells = 0
for i in range(15): #the quantity of the objects
    Cell = cell()
    cells.append(Cell)

#-------------------- main loop ----------------------
def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type== QUIT: #if pressing the X, quit the programe
                pygame.quit() #Halts the game (uninitialise)
                sys.exit() #Halts the game program
        framework.fill((WHITE)) #clears the background
        for i in cells: #update all cells
            i.wander()
            i.draw()
        pygame.display.update() #update display
        pygame.time.Clock().tick(FPS) #limit FPS

mainloop()

pygame.init() 

#coordinates for the different values of the RectsValues variable
Xpos = 65
Ypos = 35

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
black    = (30,  30,   30) 
white    = (192, 192, 192) 
green    = (32,  178, 170)
blue     = (50,  120, 220)
yellow   = (255, 215,   0)
red      = (255,  69 ,  0)
lavender = (230, 230, 250)

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
Pointer         = 'Option1'
ObjectsValue    = 1
RectsValue      = 1
 
#Reference: Learned how to do that function in one of the videos of TheNewBoston
def text_objects(text, color, FontName):
    textSurface = FontName.render(text,True,color)
    return textSurface, textSurface.get_rect()

# Function to show a message to the screen
def text_to_screen(text,color,FontName,pos):
    textSurf, textRect = text_objects(text,color,FontName)
    textRect.center = ((displayWidth/2)),(pos)
    displaySurface.blit(textSurf,textRect)

#Intro/Menu    
def Menu(): 

    global Pointer, ObjectsColour, ObjectsValue, RectsColour, RectsValue, STARTcolour, startGame, shape1colour, shape2colour, shape3colour, shape4colour

    Menu = True

    #the Menu loop will run untill ENTER (RETURN) is pressed and will then call the Game function which is basically the game itself
    while Menu: 
        
        #GUI Menu
        displaySurface.fill(black)
        shape1 = pygame.draw.rect(displaySurface, shape1colour, (468, 199, 6, 6))
        shape2 = pygame.draw.rect(displaySurface, shape2colour, (498, 199, 6, 6))
        shape3 = pygame.draw.rect(displaySurface, shape3colour, (459, 259, 6, 6))
        shape4 = pygame.draw.rect(displaySurface, shape4colour, (491, 259, 6, 6))
        pygame.draw.line(displaySurface, blue, (30,102),(205, 102), 2)
        pygame.draw.line(displaySurface, blue, (597,102),(771, 102), 2)
        text_to_screen('Objects:   ' + str(ObjectsValue), ObjectsColour, fontType,200) # add text to screen
        text_to_screen('Rects:     ' + str(RectsValue), RectsColour, fontType,260) # add text to screen
        text_to_screen('Welcome to WRECT', blue, fontType, 100)
        text_to_screen('PRESS ENTER TO START GAME', STARTcolour, fontType2,370) # add text to screen
        text_to_screen('ESC TO CLOSE THE GAME', STARTcolour, fontType3,415)

        #This part makes the last two messages to the screen blink
        if STARTcolour == blue:
            STARTcolour = black
            time.sleep(0.15)
        elif STARTcolour == black:
            STARTcolour = blue
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
                        shape1colour = green
                        shape2colour = green
                        shape3colour = white
                        shape4colour = white
                        RectsColour = white
                        Pointer = 'Option2'
                if event.key == pygame.K_UP:
                    if Pointer == 'Option2':
                        ObjectsColour = white
                        shape1colour = white
                        shape2colour = white
                        shape3colour = green
                        shape4colour = green
                        RectsColour = green                        
                        Pointer = 'Option1'
                if event.key == pygame.K_RIGHT:
                    if Pointer == 'Option1':
                        if ObjectsValue < 5:
                            ObjectsValue += 1
                    if Pointer == 'Option2':
                        if RectsValue < 5:
                            RectsValue += 1
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
                    

#Main Game
def Game():  

    global Pointer,ObjectsColour, Ypos, Xpos, Ypos1, Xpos1, Ypos2, Xpos2, Ypos3, Xpos3, Ypos4, Xpos4, RectsColour,ObjectsValue,RectsValue, STARTcolour, startGame, shape1colour, shape2colour, shape3colour, shape4colour

    Game = True
    
    #main game loop #####(handles events, updates the game state, draws the game state to the screen)
    while Game: 

        #Border should be drawn here 
        displaySurface.fill(white)
        
        if RectsValue == 1:
            rect1 = pygame.draw.rect(displaySurface, lavender,[Xpos,  Ypos, 20, 20])
        elif RectsValue == 2:
            rect1 = pygame.draw.rect(displaySurface, lavender,[Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
        elif RectsValue == 3:
            rect1 = pygame.draw.rect(displaySurface, lavender,[Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
        elif RectsValue == 4:
            rect1 = pygame.draw.rect(displaySurface, lavender,[Xpos,  Ypos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
            rect4 = pygame.draw.rect(displaySurface, lavender,[Xpos3, Ypos3, 20, 20])
        elif RectsValue == 5:
            rect1 = pygame.draw.rect(displaySurface, lavender,[Xpos,  Xpos, 20, 20])
            rect2 = pygame.draw.rect(displaySurface, lavender,[Xpos1, Ypos1, 20, 20])
            rect3 = pygame.draw.rect(displaySurface, lavender,[Xpos2, Ypos2, 20, 20])
            rect4 = pygame.draw.rect(displaySurface, lavender,[Xpos3, Ypos3, 20, 20])
            rect5 = pygame.draw.rect(displaySurface, lavender,[Xpos4, Ypos4, 20, 20])
           
            
        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
            #if enter pressed, all drawn rectangles will move to some location
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        Xpos  = random.randint(25,500)
                        Ypos  = random.randint(25,480)
                        Xpos1 = random.randint(25,500)
                        Ypos1 = random.randint(25,480)
                        Xpos2 = random.randint(25,500)
                        Ypos2 = random.randint(25,480)
                        Xpos3 = random.randint(25,500)
                        Ypos3 = random.randint(25,480)
                        Xpos4 = random.randint(25,500)
                        Ypos4 = random.randint(25,480)
                      
                      
                #####exit game even while it is running // can change later to ****PAUSE*********!!!!!!
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit
                ####maybe add pop-up alert to ask if the player is sure if they want to exit the game while it is
                #### #still running................
            
Menu()

pygame.init()

gameExit = False
gameDisplay = pygame.display.set_mode((500, 500))
l_x = 300
l_y = 300
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
    else:
        pygame.draw.rect(gameDisplay, white, whiteSquare)

    points = reward(points)
    
    print(points)
        
    pygame.display.update()

    clock.tick(FPS)
    pygame.display.update()


