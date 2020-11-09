import modules

def foundmonster(currentUser, monster_data, gold):
    data = []
    for i in monster_data:
        if i[0] != "ID":
            data = data + [i]

    monster = modules.randomchoice(data)
    print("You have met a "+ monster[1] +", will you fight or will you flee ( luck * 10% )?\n"+monster[1]+" stats: \nAttack:",monster[2] ,"\nDefense:", monster[3],"\nHealth:", monster[4])
    result = str(input("$ "))

    if result == "fight":
        endfight = False
        quit = False
        newChar = False
        currentUser , quit, newChar, gold = fight(monster, currentUser, endfight, quit, newChar, gold)

        return currentUser, quit ,newChar, gold

    elif result == "flee":
        quit = False
        newChar = False

        return currentUser, quit, newChar, gold

def fight(monster, currentUser, endfight, quit, newChar, gold):
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
                    monster[3] = "0"
                    print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar)

                else:
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar)
            
            elif int(monster[3]) <= 0:
                if int(monster[4]) <= 0:
                    print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                    gold, currentUser = win(currentUser, gold)
                    quit = False
                    newChar = False
                    endfight = True

                elif int(monster[4]) > 0:
                    monsterHP = int(monster[4]) - int(currentUser[5])

                    if monsterHP > 0:
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar)

                    elif monsterHP <= 0:
                        print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                        gold, currentUser = win(currentUser,gold)
                        quit = False
                        newChar = False
                        endfight = True
        
        elif result == "magic":

            if int(monster[3]) > 0:
                dmg = int(monster[3]) - int(currentUser[6])
                monster[3] = str(dmg)

                if dmg < 0:
                    dmg = -dmg
                    HP = int(monster[4]) - dmg
                    monster[4] = str(HP)
                    monster[3] = "0"
                    print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])

                else:
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar)
            
            elif int(monster[3]) <= 0:

                if int(monster[4]) <= 0:
                    print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                    gold, currentUser = win(currentUser, gold)
                    quit = False
                    newChar = False
                    endfight = True

                elif int(monster[4]) > 0:
                    monsterHP = int(monster[4]) - int(currentUser[5])

                    if monsterHP > 0:
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar)

                    elif monsterHP <= 0:
                        print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                        gold, currentUser = win(currentUser, gold)
                        quit = False
                        newChar = False
                        endfight = True
        
        elif result == "flee":
            quit = False
            newChar = False
            endfight = True

    return currentUser , quit, newChar , gold

def fightback(monster,currentUser,quit,newChar):
    if int(currentUser[7]) > 0:
        dmg = int(currentUser[7]) - int(monster[2])
        currentUser[7] = str(dmg)

        if dmg < 0:
            dmg = -dmg
            HP = int(currentUser[3]) - dmg
            currentUser[3] = str(HP)
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

    elif int(currentUser[7]) <= 0:
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

    elif int(currentUser[3]) <= 0:
        currentUser[3] = "0"
        print("Game over!\nYou can create a new character or quit game.")
        result = str(input("$ "))
        if result == "newChar":
            newChar = True
            quit = False
            endfight = True

            return newChar, quit, currentUser , endfight
        
        elif result == "exit":
            newChar = False
            quit = True
            endfight = True

            return newChar, quit, currentUser , endfight

def win(currentUser,gold):
    print("You have won the fight! \nGot 10 gold \nExperience + 50")
    gold = gold + 10
    exp  = int(currentUser[9]) + 50
    currentUser[9] = str(exp)

    return gold, currentUser



