import random
import string

class Hero:

    def __init__(self, n, l, r, c, h, s, a, w, d):
        self.name = n
        self.race = r
        self.level = l
        
        #class
        self.cl = c
        self.strength = s
        self.agility = a
        self.wisdom = w
        self.health_base = h
        self.health_max = (h+h*l) // 2
        self.health_curr = (h+h*l) // 2
        self.dirarray = d

    def __str__(self):
        return "{}, Level {} {} {}".format(self.name, self.level, self.race, self.cl)
    #def trapTap(dmg, defuse, dodge):
        #if 


def generateName(r, c):
    v = ["a", "e", "i", "o", "u"]
    add = ["b", "d", "m", "r"]
    end = ["a", "c", "d", "e", "k", "x", "z"]
    
    l_one = "t"
    l_two = "e"
    l_three = "s"
    l_four = "t"
    
    if(r == "Voleman"):
        if(c == "Boor"):
            l_one = "Bi"
            l_two = "vil"
        else:
            l_one = "Vi"
            l_two = "l"

            
    elif(r == "Gnoll"):
        l_one = "Do'"
        l_two = random.choice(add) + random.choice(v)
        
    elif(c == "Boor"):
        l_one = random.choice(add).upper()
        l_two = "o"
        
    else:
        l_one = random.choice(string.ascii_uppercase)
        l_two = random.choice(v)
        
    if(r != "Ogre"):
        #adgjmpsvy
        l_three = random.choice(string.ascii_lowercase[0::3])
        l_four = random.choice(end)



    if(l_one == "Q" and l_two != "u"):
        l_one = l_one + "u"

    elif(l_one == "X"):
        if "Elf" in r:
            l_one = "Xe"
            l_two = "th"
        else:
            l_one = "X"
            l_two = "e"
        
    elif(l_one == "A"):
        l_one = l_one + random.choice(add)

    if(r != "Ogre"):
        if(l_two == "i" and l_three == "j"):
            
            if(c == "Zealot"):
                l_three = "'ze"
            else:
                l_two = "y"
                l_three = ""
        
        elif(l_two == l_three or l_two == "v"):
            l_two = l_two + random.choice(end) + "'"
            l_three = random.choice(end) + l_three

            
        if(l_four != "a" and l_three not in v):
            l_four = random.choice(v) + l_four

        if("e" == l_four and (c == "Chevalier" or c == "Stalwart")):
            l_four = "ed"
            l_two = "t" + l_two
        
        if(("k" in l_four or "c" in l_four or "a" in l_four) and r == "Troll"):
            l_four = l_four + "k"

        elif("z" in l_four and r == "Kurz Elf"):
            l_four = l_four + "z"

        elif("z" in l_four and r == "Klug Elf"):
            l_four = "igg"
            
        return l_one + l_two + l_three + l_four
    
    else:
        return l_one + l_two + random.choice(add)
    
def generateHeroRandom(level, races, classes):
    
    cr = random.choice(races)

    rantemp = random.randint(0, 3)
    if((cr[0] == "Gnoll" or cr[0] == "Ogre") and rantemp == 0):
       cc = random.choice([["Boor", 3, 3, 0, 0], ["Brute", 6, 2, 0, 0]])
    else:
       cc = random.choice(classes)
    
    name = generateName(cr[0], cc[0])

    mod_h = 0
    mod_s = 0
    mod_a = 0
    mod_i = 0

    
    if(name == "Kodax" and cc == "Wayfinder"):
        mod_i += 1
        mod_h -= 3
        name = "Kodax the Vision"
        
    elif(name == "Jesux"):
        if(cc[0] == "Zealot" or cc[0] == "Sage" or cc[0] == "Wayfinder"):
            mod_h += 6
            mod_s += 1
            mod_a += 1
            mod_i += 10
            name = "Son of the Order"
        elif(cc[0] == "Brute" or cc[0] == "Vagabond" or cc[0] == "Brigand"):
            mod_h += 6
            mod_s += 6
            mod_a += 6
            name = "Beast of the Order"
        else:
            name = "Judix"
            
    elif(name == "Mega"):
        mod_h += 12
        mod_s += 3
        mod_a += 3
        name = "MEGAFIST"
        
    return Hero(name, level, cr[0], cc[0], cr[1]+cc[1]+mod_h, cr[2]+cc[2]+mod_s, cr[3]+cc[3]+mod_a, cr[4]+cc[4]+mod_i, cr[5])
