#main.py
#Jordan Tuck

import Tile as t
import Solve as s
import Hero as h

import random
import copy
import os

#random seed
random.seed()
#generation of tile map
tmap = t.TileMap(-1, -1, -1, -1, -1, -1)
tmap.readFile()
#races
r = [["Human", 11, 3, 3, 3, ["left", "up", "right", "down"]]]
r.append(["Gnoll", 11, 4, 4, 1, ["up", "down", "right", "left"]])
r.append(["Troll", 11, 5, 2, 2, ["up", "left", "down", "right"]])
r.append(["Kurz Elf", 8, 2, 5, 3, ["right", "up", "left", "down"]])
r.append(["Goblin", 8, 1, 8, 1, ["right", "down", "up", "left"]])
r.append(["Ogre", 11, 7, 1, 1, ["down", "right", "up", "left"]])
r.append(["Klug Elf", 8, 2, 3, 5, ["right", "up", "left", "down"]])
r.append(["Fleshwork", 8, 6, 4, 0, ["down", "up", "left", "right"]])
r.append(["Voleman", 8, 0, 8, 0, ["down", "left", "right", "up"]])
#classes
c = [["Vagabond", 3, 1, 1, 1]]
c.append(["Sage", 0, 0, 0, 4])
c.append(["Courier", 0, 0, 4, 0])
c.append(["Speleologist", 0, 2, 0, 2])
c.append(["Brigand", 0, 1, 3, 0])
c.append(["Boor", 3, 3, 0, 0])
c.append(["Explorer", 3, 0, 1, 2])
c.append(["Bandit", 3, 1, 2, 0])
c.append(["Wayfinder", 0, 0, 2, 2])
c.append(["Stalwart", 3, 1, 0, 2])
c.append(["Brute", 6, 2, 0, 0])
c.append(["Chevalier", 6, 0, 2, 0])
c.append(["Zealot", 6, 0, 0, 2])

stepcount = 0.
testcount = 10


for x in range(testcount):
    #solve the maze with a copy of the maze, limit of steps, and random hero
    s.solveQRS(copy.deepcopy(tmap), 1000000, h.generateHeroRandom(1, r, c))
    input()
    #clear system
    os.system("cls")

input("Press enter to continue")
