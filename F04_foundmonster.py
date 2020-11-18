import modules, F10_help

def foundmonster(currentUser, monster_data):
    endfight = False
    data = []
    for i in monster_data:
        if i[0] != "ID":
            data = data + [i]
    monster = modules.randomchoice(data)

    while (not endfight):
        quit = False
        newChar = False

        print("You have met a "+ monster[1] +", will you fight or will you flee ?\n"+monster[1]+" stats: \nAttack:",monster[2] ,"\nDefense:", monster[3],"\nHealth:", monster[4])
        result = str(input("$ "))

        if result == "fight":
            currentUser , quit, newChar, endfight = fight(monster, currentUser, endfight, quit, newChar)

            return currentUser, quit, newChar
        elif result == "flee":
            result = modules.randomrange(501)
            if result >= (500 - int(currentUser[8])):

                return currentUser, quit, newChar
            else:
                print("Bad luck ! You can't run from the monster")
                currentUser , quit, newChar, endfight = fight(monster, currentUser, endfight, quit, newChar)

                return currentUser, quit, newChar

def fight(monster, currentUser, endfight, quit, newChar):
    while (not endfight):
        print("What action will you take?\n1. strike - "+ currentUser[5] +"\n2. magic - "+ currentUser[6] +"\n3. flee")
        result = str(input("$ "))
        if result == "strike":
            if int(monster[3]) > 0:
                dmg = int(monster[3]) - int(currentUser[5])
                monster[3] = str(dmg)

                if dmg < 0:
                    dmg = -dmg
                    HP = int(monster[4]) - dmg
                    monster[4] = str(HP)
                    if int(monster[4]) <= 0:
                        print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)

                    else:
                        monster[3] = "0"
                        print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                else:
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)
            
            else:

                if int(monster[4]) <= 0:
                    print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                    currentUser = win(currentUser, monster)
                    quit = False
                    newChar = False
                    endfight = True

                else:
                    monsterHP = int(monster[4]) - int(currentUser[5])

                    if monsterHP > 0:
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                    else:
                        print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)
        
        elif result == "magic":

            if int(monster[3]) > 0:
                dmg = int(monster[3]) - int(currentUser[6])
                monster[3] = str(dmg)

                if dmg < 0:
                    dmg = -dmg
                    HP = int(monster[4]) - dmg
                    monster[4] = str(HP)
                    if int(monster[4]) <= 0:
                        print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)

                    else:
                        monster[3] = "0"
                        print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                else:
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)
            
            else:

                if int(monster[4]) <= 0:
                    print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                    currentUser, newChar, quit, endfight = win(currentUser, monster)

                else:
                    monsterHP = int(monster[4]) - int(currentUser[6])

                    if monsterHP > 0:
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                    else:
                        print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)
        
        elif result == "help":
            section = 1
            F10_help.help(section)

        elif result == "flee":
            result = modules.randomrange(501)
            if result >= (500 - int(currentUser[8])):
                quit = False
                newChar = False
                endfight = True

            else:
                print("Bad luck ! You can't run from the monster")
                newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

    return currentUser , quit, newChar, endfight

def fightback(monster,currentUser,quit,newChar,endfight):
    if int(currentUser[7]) > 0:
        dmg = int(currentUser[7]) - int(monster[2])
        currentUser[7] = str(dmg)

        if dmg < 0:
            dmg = -dmg
            HP = int(currentUser[3]) - dmg
            currentUser[3] = str(HP)
            if int(currentUser[3]) <= 0:
                print(monster[1],"strike for "+ str(dmg) +" dmg")
                currentUser[3] = "0"
                print("Game over!\nYour character is die.\nYou can create a new character or quit game.")
                result = str(input("$ "))

                if result == "create":
                    newChar = True
                    quit = False
                    endfight = True

                    return newChar, quit, currentUser , endfight

                elif result == "exit":
                    newChar = False
                    quit = True
                    endfight = True

                    return newChar, quit, currentUser , endfight
            
            else:
                currentUser[7] = "0"
                print(monster[1],"strike for "+ str(dmg) +" dmg")
                newChar = False
                quit = False
                endfight = False

                return newChar, quit, currentUser, endfight

        else:
            print(monster[1],"strike for 0 dmg")
            quit = False
            newChar = False
            endfight = False

            return newChar, quit, currentUser, endfight

    else:

        if int(currentUser[3]) <= 0:
            print(monster[1],"strike for "+ str(monster[2]) +" dmg")
            currentUser[3] = "0"
            print("Game over!\nYour character is die.\nYou can create a new character or quit game.")
            result = str(input("$ "))

            if result == "create":
                newChar = True
                quit = False
                endfight = True

                return newChar, quit, currentUser , endfight

            elif result == "exit":
                newChar = False
                quit = True
                endfight = True

                return newChar, quit, currentUser , endfight

        else:
            HP = int(currentUser[3]) - int(monster[2])
            currentUser[3] = str(HP)
            newChar, quit, currentUser, endfight = shieldbroken(currentUser,monster,HP,quit,newChar)

    return newChar, quit, currentUser, endfight

def shieldbroken(currentUser,monster,HP,quit,newChar):
    if int(currentUser[3]) > 0:
        currentUser[3] = str(HP)
        print(monster[1],"strike for "+ str(monster[2]) +" dmg")
        newChar = False
        quit = False
        endfight = False

        return newChar, quit, currentUser, endfight

    else:
        print(monster[1],"strike for "+ str(monster[2]) +" dmg")
        currentUser[3] = "0"
        print("Game over!\nYour character is die.\nYou can create a new character or exit game.")
        result = str(input("$ "))

        if result == "create":
            newChar = True
            quit = False
            endfight = True

            return newChar, quit, currentUser , endfight
        
        elif result == "exit":
            newChar = False
            quit = True
            endfight = True

            return newChar, quit, currentUser , endfight

def win(currentUser, monster):
    if monster[1] == "Alduskuy":
        print("You have won the fight! \nGot 10000 gold \nExperience + 1000")
        gold = int(currentUser[12]) + 10000
        exp  = int(currentUser[9]) + 1000
        currentUser[12] = str(gold)
        currentUser[9] = str(exp)
        print("Do you want to create a new character or exit?")
        result = str(input("$ "))

        if result == "create":
            newChar = True
            quit = False
            endfight = True

            return currentUser, newChar, quit, endfight

        elif result == "exit":
            newChar = False
            quit = True
            endfight = True

            return currentUser, newChar, quit, endfight

    else:
        print("You have won the fight! \nGot 10 gold \nExperience + 50")
        gold = int(currentUser[12]) + 10
        exp  = int(currentUser[9]) + 50
        currentUser[9] = str(exp)
        currentUser[12] = str(gold)
        newChar = False
        quit = False
        endfight = True

        return currentUser, newChar, quit, endfight



