import Hero as h

test = h.Hero("Steve", 69, "Human", "Bard", 10, 10, 10, 10, ["left, up, right, down"])


r = [["Human", 11, 3, 3, 3, ["left", "up", "right", "down"]]]
r.append(["Gnoll", 11, 4, 4, 1, ["up", "down", "right", "left"]])
r.append(["Troll", 11, 5, 2, 2, ["up", "left", "down", "right"]])
r.append(["Kurz Elf", 8, 2, 5, 3, ["right", "up", "left", "down"]])
r.append(["Goblin", 8, 1, 8, 1, ["right", "down", "up", "left"]])
r.append(["Ogre", 11, 7, 1, 1, ["down", "right", "up", "left"]])
r.append(["Klug Elf", 8, 2, 3, 5, ["right", "up", "left", "down"]])
r.append(["Fleshwork", 8, 6, 4, 0, ["down", "up", "left", "right"]])
r.append(["Voleman", 8, 0, 8, 0, ["down", "left", "right", "up"]])

c = [["Vagabond", 3, 1, 1, 1]]
c.append(["Sage", 0, 0, 0, 4])
c.append(["Speleologist", 0, 2, 0, 2])
c.append(["Brigand", 0, 1, 3, 0])
c.append(["Boor", 3, 3, 0, 0])
c.append(["Courier", 0, 0, 4, 0])
c.append(["Explorer", 3, 0, 1, 2])
c.append(["Bandit", 3, 1, 2, 0])
c.append(["Wayfinder", 0, 0, 2, 2])
c.append(["Stalwart", 3, 1, 0, 2])
c.append(["Brute", 6, 2, 0, 0])
c.append(["Chevalier", 6, 0, 2, 0])
c.append(["Zealot", 6, 0, 0, 2])


gnoll_a = 0
gnoll_b = 0
gnoll_total = 0

other_a = 0
other_b = 0
other_total = 0

for x in range(1000000):
    test = h.generateHeroRandom(1, r, c)
    print(test)
    print("Health:", test.health_max, "Str/Agi/Int:", test.strength, test.agility, test.wisdom)
    print()
    input()
    
##    if(test.race == "Ogre" or test.race == "Gnoll"):
##        if(test.cl == "Boor" or test.cl == "Brute"):
##            gnoll_a += 1
##        else:
##            gnoll_b += 1
##            
##        gnoll_total += 1
##        
##    else:
##        if(test.cl == "Boor" or test.cl == "Brute"):
##            other_a += 1
##        else:
##            other_b += 1
##            
##        other_total += 1
    
