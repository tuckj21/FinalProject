###Jordan Tuck
###Senior Project
###CS 491

###Program for generating a maze

###Simple object that holds a few IDs and traits
    
class Tile:
    state = 0
    mark = 0
    health = 0 
    dmg = 0
    hero = False
    
    def __init__(self, state, mark, health, dmg):
        self.state = state
        self.mark = mark
        self.health = health
        self.dmg = dmg
        
###More complex object that houses both lots of tiles and info
class TileMap:

    ##x, y = dimensions of the maze 
    x = 4
    y = 4
    
    ##ent = entrance, or "start" of the maze
    ##exit = exit, or ending point of the maze
    entx = 1
    enty = 1

    ##object creation
    ##i, j = input of x, y
    ##en_x, en_y = imput of ent
    ##ex_x, ex_y = imput of exit
    def __init__(self, i, j, en_x, en_y, ex_x, ex_y):
        if(i > 4):
            self.x = i
        if(j > 4):
            self.y = j
            
        self.entx = en_x
        self.enty = en_y
        self.exitx = ex_x
        self.exity = ex_y

        if(en_x <= 0 or en_x >= (self.x - 1) or en_y <= 0 or en_y >= (self.y - 1)):
            self.entx = 1
            self.enty = 1
        if(ex_x <= 0 or ex_x >= (self.x - 1) or ex_y <= 0 or ex_y >= (self.y - 1)):
            self.exitx = self.x - 2
            self.exity = self.y - 2
        if(en_x == ex_x and en_y == ex_y):
            self.entx = 1
            self.enty = 1
            self.exitx = self.x - 2
            self.exity = self.y - 2

        self.tarray = [[Tile(0, 0, 0, 0) for m in range(self.x)] for n in range(self.y)]
        
        for n in range(self.y):
            for m in range(self.x):
                if(m == 0 or m == (self.x - 1) or n == 0 or n == (self.y - 1)):
                    self.tarray[n][m] = Tile(1, 0, 0, 0)
                elif(m == self.entx) and (n == self.enty):
                    self.tarray[n][m] = Tile(2, 0, 0, 0)
                elif(m == self.exitx) and (n == self.exity):
                    self.tarray[n][m] = Tile(3, 0, 0, 0)
        
        
    def tilePrint(self):
        printout = ""
        for n in range(self.y):
            parray = ""
            for m in range(self.x):
                
                t = self.tarray[n][m]
                
                ####i miss switch cases
                ####granted, could make it myself but whatever
                
                ###Prints out based off of state of character and if it's been stepped on

                ## Open Area
                if (t.state == 0):
                    ##If hero is here
                    if(t.hero == True):
                        parray += ("{:2}".format('@'))
                    ##Else open
                    else:
                        parray += ("{:2}".format(' '))
                        
                ## Wall
                elif (t.state == 1):
                    parray += ("{:2}".format('#'))
                elif (t.state == 2):
                    parray += ("{:2}".format('('))
                elif (t.state == 3):
                    parray += ("{:2}".format(')'))
                elif (t.state == 5):
                    parray += ("{:2}".format('X'))
                
                elif (t.state == 7):
                    parray += ("{:2}".format('*'))
                elif (t.state == 8):
                    parray += ("{:2}".format('#'))
                elif (t.state == 9):
                    parray += ("{:2}".format('T'))
                
                else:
                    parray += ("{:2}".format('?'))
                    #print('?', end = '')
            printout += parray + "\n"
        print(printout)

            
    def readFile(self):
        with open("TileSet.txt") as file:
            ta = [line.rstrip() for line in file]
            #ta = [line.rstrip().split(' ') for line in file]
            self.y = len(ta)
            self.x = len(ta[0])
            self.tarray = [[Tile(0, 0, 0, 0) for m in range(self.x)] for n in range(self.y)]
            n = 0
            for line in ta:
                m = 0
                for char in line:
                    if(char == '.'):
                        self.tarray[n][m].mark = 1
                    elif(char == '#'):
                        self.tarray[n][m].state = 1
                    elif(char == '('):
                        self.tarray[n][m].state = 2
                        self.entx = m
                        self.enty = n
                    elif(char == ')'):
                        self.tarray[n][m].state = 3
                        self.exitx = m
                        self.exity = n
                    elif(char == '*'):
                        self.tarray[n][m].state = 7
                        self.tarray[n][m].health = 10
                        self.tarray[n][m].dmg = 10
                    elif(char == '#'):
                        self.tarray[n][m].state = 8
                        self.tarray[n][m].health = 10
                        self.tarray[n][m].dmg = 10
                    elif(char == 'T'):
                        self.tarray[n][m].state = 9
                        self.tarray[n][m].health = 10
                        self.tarray[n][m].dmg = 10
                    m += 1
                n += 1

###Simple function for shifting the direction of maze solvers
