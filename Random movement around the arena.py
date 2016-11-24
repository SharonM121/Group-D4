import pygame   #importing pygame module from library
import random    #the random module implements a random number generator
import sys #with this a number of functions and variables that can be used to manipulate different parts of the Python runtime environment
from pygame.locals import * #imports the pygame module into the "pygame" namespace

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
cells = []
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

