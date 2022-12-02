def alphabet_war(fight):
    a = 0
    for i in fight:
        if i == "w":
            a = a + 4
        elif i == "p":
            a = a + 3
        elif i == "b":
            a = a + 2
        elif i == "s":
            a = a + 1
        elif i == "m":
            a = a - 4
        elif i == "q":
            a = a - 3
        elif i == "d":
            a = a - 2
        elif i == "z":
            a = a - 1
                   
    if a > 0:
        return  "Left side wins!"
    elif a == 0:
        return "Let's fight again!"
    else:
        return "Right side wins!"
