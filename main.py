# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import F01_createdragonborn, F02_attribute, F03_explore, F04_foundmonster, F05_foundgold, F06_shopping, F07_levelup, F08_alduskuy, F09_switchcity, F10_help, F11_saveandloadgame, F12_exitgame,F14_sidequest

'''
Zachrandika Alif Syahreza
Dimas Farhan Anshari
Ali Zayn Murteza
Muhammad Erwin Fattah
Muhammad Farhan
'''


# KAMUS GLOBAL
'''
    dragonborn_data : array of array of string
    item_data       : array of array of string
    monster_data    : array of array of string
    sidequest_data  : array of array of string
'''

endprogram  = False
currentUser = [" $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]

print("Welcome to Skuyrim")
dragonborn_data, item_data, sidequest_data = F11_saveandloadgame.load()

print("Choose your character or create new character :")
newChar, currentUser = F11_saveandloadgame.dataload (dragonborn_data, currentUser)
if (newChar):
    dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

while (not endprogram):
    monster_data = F11_saveandloadgame.loadmonster()

    increaselevel = int(currentUser[9]) // 100
    if increaselevel > int(currentUser[4]):
        currentUser = F07_levelup.levelup(currentUser, increaselevel)

    command = str(input("$ "))

    if   command == "status":
        F02_attribute.attribute(currentUser)

    elif command == "explore":
        result = F03_explore.explore(currentUser)
        if (result):
            currentUser = F05_foundgold.foundgold(currentUser)

        else:
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster_data)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "shopping":
        currentUser = F06_shopping.shop(currentUser, item_data)

    elif command == "alduskuy":
        foundmonster = False
        foundmonster, monster = F08_alduskuy.alduskuy(foundmonster)
        if (foundmonster):
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "switch city":
        print("hello")
        foundmonster = False
        currentUser, foundmonster = F09_switchcity.switchcity(currentUser, foundmonster)
        if(foundmonster):
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster_data)
            if (quit):
                simpan = F12_exitgame.exit()
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "help":
        section = 0
        F10_help.help(section)
        
    elif command == "list sidequest":
        F14_sidequest.sidequest(sidequest_data,currentUser)
        
    elif command == "save":
        data = [dragonborn_data, item_data, sidequest_data]
        names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
        F11_saveandloadgame.save(data, names, currentUser)

    elif command == "exit":
        simpan = F12_exitgame.exit()
        if (simpan):
            data = [dragonborn_data, item_data, sidequest_data]
            names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
            F11_saveandloadgame.save(data, names, currentUser)

        print("Thanks for playing skuyrim, goodbye!")
        endprogram = True