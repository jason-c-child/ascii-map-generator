# - ascii map generator

import random
import argparse
import hashlib

# - Lists of rectangles
shapes0 = {
    1:{"x": 1, "y": 1},
    2:{"x": 1, "y": 2},
    3:{"x": 2, "y": 1}
}

shapes1 = {
    1:{"x": 10, "y": 10},
    2:{"x": 15, "y": 8},
    3:{"x": 7, "y": 3},
    4:{"x": 12, "y": 5},
    5:{"x": 20, "y": 2}
}

shapes2 = {
    1:{"x": 30, "y": 5},
    2:{"x": 20, "y": 6},
    3:{"x": 25, "y": 5}
}

shapes3 = {
    1:{"x": 10, "y": 50},
    2:{"x": 15, "y": 75},
    3:{"x": 5, "y": 100}
}

shapes4 = {
    1:{"x": 7, "y": 2},
    2:{"x": 6, "y": 3},
    3:{"x": 5, "y": 4}
}

shapes5 = {
    1:{"x": 70, "y": 30}
}

presets = {
    "1 - Pocket sized" : {"Set": 1, "a": 15, "b": 25, "shapes": shapes1, "c": 2, "l": 5, "p": "T"},
    "2 - Long" : {"Set": 2, "a": 500, "b": 100, "shapes": shapes3, "c": 3, "l": 100, "p": "T"},
    "3 - Mess" : {"Set": 3, "a": 36, "b": 100, "shapes": shapes0, "c": 0, "l": 1000, "p": "F"},
    "4 - Box" : {"Set": 4, "a": 36, "b": 100, "shapes": shapes2, "c": 0, "l": 20, "p": "T"},
    "5 - Islands" : {"Set": 5, "a": 25, "b": 75, "shapes": shapes4, "c": 0, "l": 25, "p": "T"},
    "6 - Waterland" : {"Set": 6, "a": 20, "b": 50, "shapes": shapes0, "c": 1, "l": 1500, "p": "F"},
    "7 - Blob" : {"Set": 7, "a": 36, "b": 100, "shapes": shapes5, "c": 20, "l": 3, "p": "F"},
}

# Function that creates the basic map, defines stuff like size, legend, positions on left/right side, ect
def generate_basemap(s, preset_arg):
    global MAP
    global stuff
    global PIL
    global Legend 
    global shapes
    global presets
    global l
    global a
    global b
    global A
    global c
    global LS 
    global RS
    global p
    stuff = ["*", "@", "%", "$", "#"]
    PIL = []
    MAP = {}
    if s == "1":
        shapes = shapes1
        l = 7
        c = 2
        a = 18
        b = 40
        p = "T"
    elif s == "2":
        shapes = shapes2
        l = 15
        c = 3
        a = 36
        b = 100
        p = "T"
    elif s == "3":
        shapes = shapes2
        l = 50
        c = 4
        a = 48
        b = 191
        p = "T"
    else:
        cmd = int(preset_arg)
        for i in presets:
            if presets[i]["Set"] == cmd:
                shapes = presets[i]["shapes"]
                l = presets[i]["l"]
                c = presets[i]["c"]
                a = presets[i]["a"]
                b = presets[i]["b"]
                p = presets[i]["p"]
    A = a*b
    MAP = {}
    for x in range(A):
        MAP[x] = "~"
    RS = [b]
    LS = [0]
    i = 0
    y = 0
    while i != a:
        y += b
        LS.append(y)
        i += 1
    i = 0
    y = 0
    while i != a:
        y += b
        RS.append(y)
        i += 1

# Functions that name stuff
def name_map():
    FP = lambda: random.choice(
        [
            "Str",
            "Tra",
            "Kle",
            "Olc", 
            "Mat", 
            "Wir", 
            "Sle", 
            "Pad", 
            "Lat", 
            "Far",
            "Tel",
            "Vor",
            "Elm",
            "Loi",
            "Pel",
            "Kor",
            "Ble",
            " Ar",
            " En",
            " Ka",
            " Vo",
            " Li",
            " Xe",
            " Ze",
            " Zo",
            " Xi",
            " La",
            " Bi",
            " Er",
            " Om",
            " Ra",
            "Pli",
            "Ple",
            "Bli",
            "Era",
            "Exa",
            "Zyl",
            "Zla",
            "Zal",
            "Ran",
            "Rem",
            "Rel",
            "Ral",
            "Jel",
            "Jen",
            "Jor",
            "Jux",
            "Hen",
            "Hor",
            "Har",
            "Hir",
            "Her",
            "Qua",
            "Qen",
            "Qul",
            "Qil",
            "Qan",
            "Qaz"
        ]
    )

    SP = lambda: random.choice(
        [
            "ait",
            "cre",
            "zel",
            "tor", 
            "lin", 
            "   ", 
            "ar", 
            "ken", 
            "mon",
            "ren",
            "eld",
            "   ",
            "mar",
            "olo",
            "vex",
            "awe",
            'car',
            "elg",
            "gel",
            'i   ',
            "a   ",
            "o   ",
            "y   ",
            "    ",
        ]
    )

    return f"{FP()}{SP()}"

def Hnamer():
    FP = random.choice(["Mikker","Wimmly","Jarmit", "FiFyFo", "Peeter", "Nipnoe", "Padfot", "??????"])
    SP = random.choice(["Bold  |","Stong |","Fast  |","Large |", "Small |", "Fat   |", "Stuped|", "Smart |", "Fine  |"])
    return FP + " the " + SP

def Dnamer():
    return random.choice(["Scar             |","Kainto           |","Flea             |", "Botron           |", "Frot             |", "Clotenomen       |", "Fimotrin         |", "Death            |"])

# Function that prints the map to the console
def print_map():
    global a
    global b
    global MAP
    global Legend
    c = 0
    x = 0
    i = 0
    out = ""
    for i in range(a):
        for x in range(b):
            out += f"{MAP[c]}"
            # print(MAP[c], end = "")
            x += 1
            c += 1
        try:
            out += f"{Legend[i]}\n"
            # print(Legend[i])
        except:
            out += " |                      |\n"
            # print(" |                      |")
        x = 1
        i += 1
    return out

# Function that checks if you can place a specified rectangle(Box) on a specified position(x)
def CPlaceB(x):
    global MAP
    global Box
    global a
    global b
    y = int(x/b) + 1
    t = x - ((y - 1)*b)
    if (t + shapes[Box]["x"]) <= b and (y + shapes[Box]["y"]) <= a:
        return True
    else:
        return False

# Function that places Box on x
def PlaceB(i):
    global Box
    global a
    global b
    global MAP
    y = 0
    x = 0
    while y != shapes[Box]["y"]:
        while x != shapes[Box]["x"]:
            MAP[i] = "#"
            i +=1
            x += 1
        i += (b - shapes[Box]["x"])
        y += 1
        x = 0

# Function that randomly picks a location/rectangle(box)
def AddB():
    global Box
    global A
    global b
    global a
    Box = random.choice(list(shapes.keys()))
    while True:
            i = random.randint(-1,(A))
            if CPlaceB(i) == True:
                PlaceB(i)
                return None

# Function that smooths out long corners
def apply_curves_to_map():
    global MAP
    global b
    global c
    global RS
    global LS
    t = 0
    while t <= c:
        t += 1
        for i in MAP:
            if MAP[i] == "#":
                Sides = 0
                # - U
                x = i - b
                try:
                    a = MAP[x]
                except:
                    a = "~"
                if a == "~":
                    Sides += 1
                # - U
                # - D
                x = i + b
                try:
                    a = MAP[x]
                except:
                    a = "~"
                if a == "~":
                    Sides += 1
                # - D
                # - L
                if i in LS:
                    Sides += 1
                else:
                    x = i - 1
                    try:
                        a = MAP[x]
                    except:
                        a = "~"
                    if a == "~":
                        Sides += 1
                # - L
                # - R
                if i in RS:
                    Sides += 1
                else:
                    x = i + 1
                    try:
                        a = MAP[x]
                    except:
                        a = "~"
                    if a == "~":
                        Sides += 1
                # - R
                if Sides == 4:
                    MAP[i] = "~"
                elif Sides == 1 and t <= c:
                    if random.randint(0, 50) == 1:
                        MAP[i] = "~"
                elif Sides == 2 and t <= c:
                    if random.randint(0, 3) != 1:
                        MAP[i] = "~"
                elif Sides == 3 and t <= c:
                    if random.randint(0, 5) != 1:
                        MAP[i] = "~"
                else:
                    pass

# Function that replaces the outline of the rectangles with ascii art
def replace_outline():
    global MAP
    global b
    global LS
    global RS
    for i in MAP:
        if MAP[i] == "#":
            Sides = {"U": 0, "D": 0, "L": 0, "R": 0}
            # - U
            x = i - b
            try:
                a = MAP[x]
            except:
                a = "~"
            if a == "~":
                Sides["U"] = 1
            # - U
            # - D
            x = i + b
            try:
                a = MAP[x]
            except:
                a = "~"
            if a == "~":
                Sides["D"] = 1
            # - D
            # - L
            if i in LS:
                Sides["L"] = 1
            else:
                x = i - 1
                try:
                    a = MAP[x]
                except:
                    a = MAP[i]
                if a == "~":
                    Sides["L"] = 1
            # - L
            # - R
            if i in RS:
                Sides["R"] = 1
            else:
                x = i + 1
                try:
                    a = MAP[x]
                except:
                    a = MAP[i]
                if a == "~":
                    Sides["R"] = 1
            # - R
            if Sides["U"] == 1 and Sides["D"] == 1 and Sides["R"] == 1:
                MAP[i] = ">"  
            elif Sides["U"] == 1 and Sides["D"] == 1 and Sides["L"] == 1:   
                MAP[i] = "<"
            elif Sides["U"] == 1 and Sides["R"] == 1 and Sides["L"] == 1:   
                MAP[i] = "^"
            elif Sides["R"] == 1 and Sides["D"] == 1 and Sides["L"] == 1:   
                MAP[i] = "v"
            elif (Sides["U"] == 1 and Sides["L"] == 1) or (Sides["D"] == 1 and Sides["R"] == 1):
                MAP[i] = "/"
            elif (Sides["U"] == 1 and Sides["R"] == 1) or (Sides["D"] == 1 and Sides["L"] == 1):
                MAP[i] = u"\u005C"
            elif Sides["U"] == 1:
                MAP[i] = u"\u203E"
            elif Sides["D"] == 1:
                MAP[i] = "_"
            elif Sides["L"] == 1 or Sides["R"] == 1:
                mark = random.randrange(0,10)
                if mark >= 9:
                    if (Sides["L"] == 1):
                      MAP[i] = "}"
                    else:
                        MAP[i] = "{"
                else:
                    MAP[i] = "|"
            else:
                pass

# Function that clears out overything but the sea and outline
def Clear():
    global MAP
    for i in MAP:
        if MAP[i] == "#":
            MAP[i] = " "

# Function that adds random stuff to the empty parts of the map
def add_random_features():
    global MAP
    global PIL
    global stuff
    global p
    if p == "T":
        for i in MAP:
            if MAP[i] == " ":
                if random.randint(0, 25) == 1:
                    MAP[i] = random.choice(stuff)
                    if MAP[i] not in PIL:
                        PIL.append(MAP[i])
                    if MAP[i] == "@" or MAP[i] == "&" or MAP[i] == "+" or MAP[i] == "%" or MAP[i] == "#":
                        stuff.remove(MAP[i])

# Function that creats the Legend
def create_legend(include_compase: bool = False):
    global PIL
    global Legend
    global MAP
    global b
    Name = name_map()
    Hname = Hnamer()
    Dname = Dnamer()
    Meaning = {
    "*": "Cave             |",
    "@": "Ruins            |",
    "!": "Battle           |",
    ".": "Mountain         |",
    "+": "Mintar           |",
    "%": "Forest           |",
    "&": Dname,
    "#": "Swamp            |",
    "$": "Mine             |"
    }
    Legend = {
        0: " +----------------------+",
        1: " |        " + Name + "        |",
        2: " +----------------------+"
    }
    n = 4
    for i in PIL:
        Legend[n] = " | " + i + " = " + Meaning[i]
        n += 1
    Legend[a - 1] = " +----------------------+"
    if include_compase:
        MAP[b + 2] = "N"
        MAP[b*2 + 1] = "W"
        MAP[b*2 + 2] = "+"
        MAP[b*2 + 3] = "E"
        MAP[b*3 + 2] = "S"
        

# Main loop
while True:
    # print("Small(1), Medium(2), or Large(3)")
    # print("More(4)")
    cmd = "Small(1)"
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", default="Large(3)")
    parser.add_argument("--preset", default="1")
    parser.add_argument("--populate", default="no")
    args = parser.parse_args()
    
    generate_basemap(args.size, args.preset)
    for i in range(l):
        AddB()
    print("")
    apply_curves_to_map()
    replace_outline()
    Clear()
    if args.populate != "no":
        add_random_features()
    create_legend()
    map_string = print_map()
    print(map_string)
    md = hashlib.md5()
    md.update(map_string.encode())
    print("")
    print(md.hexdigest())
    break