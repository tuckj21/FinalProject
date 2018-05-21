import Tile as t

import random
import collections
import copy
import time
import os


def dirShift(d):
    if(d == "left"):
        return [-1, 0]
    elif(d == "right"):
        return [1, 0]
    elif(d == "down"):
        return[0, 1]
    elif(d == "up"):
        return[0, -1]
    else:
        print(d, "is no good")
        return[0, 0]

##def fastTileFind(t, px, py):
##    da = ["left", "up", "right", "down"]
##    random.shuffle(da)
##    
##    finaldir = []
##    for d in da:
##        shift = dirShift(d)
##        dx = shift[0]
##        dy = shift[1]
##        temptile = t.tarray[py + dy][px + dx]
##        if(temptile.mark == 0 and temptile.state != 1 and temptile.state != 5):
##            finaldir.append(d)
##
##    if finaldir:
##        return random.choice(finaldir)
##    else:
##        return "error"
##
##
##
##def newTileFind(t, px, py, trail):
##    #print(px, py)
##    currtile = t.tarray[py][px]
##    #print(trail)
##    if(currtile.state == 1 or currtile.state == 5 or currtile.mark > 8):
##        #print("Ending")
##        return False
##    elif(currtile.mark == 0):
##        #print("Path found")
##        return True
##    else:
##        currtile.state = 5
##        da = ["left", "up", "right", "down"]
##        random.shuffle(da)
##        #print("left")
##        for d in da:
##            shift = dirShift(d)
##            dx = shift[0]
##            dy = shift[1]
##            trail.append(d)
##            testbool = newTileFind(t, px + dx, py + dy, trail)
##            if testbool:
##                #print()
##                return trail
##            trail.pop()
##            
##        trail.pop()
##        currtile.state = 0
##        return False



def quadTileFind(t, px, py, da, trail, limit):
    #valid next spots
    if(limit == 0):
        return False
    
    choices = []
    
    currtile = t.tarray[py][px]
    currtile.state = 5
    
    #da = ["left", "up", "right", "down"]

    #check every direction for a quick path
    for d in da:
        shift = dirShift(d)
        dx = shift[0]
        dy = shift[1]
        trail.append(d)
        nexttile = t.tarray[py + dy][px + dx]
        if nexttile.state != 1 and nexttile.state != 5:
            if nexttile.mark == 0:
                return trail
            else:
                choices.append(d)
        trail.pop()

    #if you can't find a quick path, expand from vaild tiles
    for c in choices:
        shift = dirShift(c)
        dx = shift[0]
        dy = shift[1]
        trail.append(c)
        
        sublimit = limit - 1
        #recursive
        testtrail = quadTileFind(t, px+dx, py+dy, da, trail, sublimit)
        #checks if false or empty
        if testtrail:
            return testtrail
        trail.pop()
    #if you can't expand, return false
    return False

    
def solveRM(tmap, step_range):
    darray = ["left", "right", "up", "down"]
    darray_temp = darray[:]
    
    direction = random.choice(darray)
    
    ##pos_x, pos_y = position of mouse
    ##dir_x, dir_y = direction of mouse
    pos_x = tmap.entx
    pos_y = tmap.enty
    shift = dirShift(direction)
    dir_x = shift[0]
    dir_y = shift[1]

    anx_limit = 10
    
    step = 0
    
    while(step_range != 0):
        currtile = tmap.tarray[pos_y][pos_x]
        nexttile = tmap.tarray[pos_y + dir_y][pos_x + dir_x]

        ##Randomly changes directions based on how often it's been to the next tile
        anxiety = anx_limit + nexttile.mark
        #anxiety = anx_limit + currtile.mark
        
        if(anxiety > int(anx_limit / 2) + anx_limit):
            anxiety = int(anx_limit / 2) + anx_limit
        
        if(nexttile.state == 1 or (random.randrange(anxiety) >= anx_limit)):
            if not darray_temp:
                ##Failed: Stuck
                currtile.state = -1
                print(step)
                print(currtile.mark)
                tmap.tilePrint()
                return False
            else:
                if(nexttile.state == 1):
                    darray_temp.remove(direction)
                direction = random.choice(darray_temp)  
                shift = dirShift(direction)
                dir_x = shift[0]
                dir_y = shift[1]
        elif(nexttile.state == 3):
            ##Passed: Hit Goal
            currtile.mark += 1
            print(step)
            tmap.tilePrint()
            return step
        else:
            darray_temp = darray[:]
            currtile.mark += 1
            pos_x += dir_x
            pos_y += dir_y
            
        if(step_range > 0):
            step_range -= 1
            
        step += 1

    ##Failed: Ran Out of Steps/Step Range Hit Max
    tmap.tilePrint()
    return False

#quick recursive search
def solveQRS(tmap, step_range, hero):

    
    ##pos_x, pos_y = position of mouse
    ##dir_x, dir_y = direction of mouse
    pos_x = tmap.entx
    pos_y = tmap.enty
    path = []
    tmap.tarray[pos_y][pos_x].mark += 1
    tmap.tarray[pos_y][pos_x].hero = True
    
    step = 0

    print(hero)
    tmap.tilePrint()
    
    while(step_range != 0 and hero.health_curr > 0):
        #if path exists, churn out a direction
        if path:
            while path:
                
                #os.system('cls')
                print("")
                print(hero)

                
                direction = path.pop()
                
                shift = dirShift(direction)
                dir_x = shift[0]
                dir_y = shift[1]

                currtile = tmap.tarray[pos_y + dir_y][pos_x + dir_x]
                currtile.hero = True
                
                tmap.tilePrint()
                
                time.sleep(15 / (40 + len(path)))
                
                if(currtile.state == 3):
                    ##Passed: Hit Goal
                    print("Found the exit!")
                    print(step)
                    #tmap.tilePrint()
                    return step
                else:
                    if(currtile.state == 9):
                        print("Took", currtile.dmg, "Damage!")
                        if(currtile.dmg >= hero.health_curr):
                            hero.health_curr = 0
                            print(hero.name, "has been incapacitated!")
                            print(step)
                            return False
                        else:
                            hero.health_curr -= currtile.dmg
                            print(hero.health_curr, "remaining.")
                        input("Press any key.")

                    currtile.hero = False
                    
                    pos_x += dir_x
                    pos_y += dir_y
                    
                if(step_range > 0):
                    step_range -= 1

                step += 1
                #if (step % 100 == 0):
                    #print(step)
                    #tmap.tilePrint()
                
                tmap.tarray[pos_y][pos_x].mark += 1
                
                
        #find a new path
        patharray = []
        y = 0
        while y < 4:
            temparray = []
            for x in range(4):
                temparray.append(hero.dirarray[(x+y) % 4])
            temppath = []
            
            if not patharray:
                temppath = quadTileFind(copy.deepcopy(tmap), pos_x, pos_y, temparray, temppath, -1)
            else:
                temppath = quadTileFind(copy.deepcopy(tmap), pos_x, pos_y, temparray, temppath, len(patharray[0]))
                
            if temppath != False:
                patharray.append(temppath)
                if len(temppath) == 1:
                    y = 4
                elif len(temppath) < len(patharray[0]):
                    patharray = [temppath]
            y += 1
        
        #if you couldn't find a path, end search
        if not patharray:
            print("Couldn't find an exit.")
            print(step)
            return False
        
        #else, reverse the path so you can just pop()
        else:
            #print(patharray)
            path = min(patharray, key=len)
            #print(path)
            path = path[::-1]
            #time.sleep(50 / (100 + len(path)))
        
    #else:
        #print(path)

    #tmap.tilePrint()
    return False
