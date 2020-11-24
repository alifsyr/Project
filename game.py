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
    endprogram      : boolean
    currentUser     : array of string
    foundmonster    : boolean
    data            : array of array of string
    names           : array of string
    increaselevel   : integer
'''

endprogram  = False
currentUser = [" $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]

print("Welcome to Skuyrim")
dragonborn_data, item_data, sidequest_data = F11_saveandloadgame.load() # Program secara automatis langsung melakukan load data

print("Choose your character or create new character :")
newChar, currentUser = F11_saveandloadgame.dataload (dragonborn_data, currentUser)  # Program memanggil fungsi dataload
if (newChar):   # Apabila pemain ingin membuat karakter baru program memanggil fungsi createdragonborn
    dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

while (not endprogram): # Program masuk kedalam kondisi ketika pemain blom memberikan command exit
    monster_data = F11_saveandloadgame.loadmonster()    # Program secara automatis langsung melakukan load data

    increaselevel = int(currentUser[9]) // 100  # Program mengecek kenaikan level
    if increaselevel > int(currentUser[4]):     # Apabila tervalidasi sudah naik level
        currentUser = F07_levelup.levelup(currentUser, increaselevel)   # Program menggil fungsi levelup

    command = str(input("$ "))  # Program meminta pemain memasukan aksi yang ingin dilakukan

    if   command == "status":
        F02_attribute.attribute(currentUser)    # Program memanggil fungsi attribute

    elif command == "explore":
        result = F03_explore.explore(currentUser)   # Program memanggil fungsi explore
        if (result):
            currentUser = F05_foundgold.foundgold(currentUser)  # Program memanggil fungsi foundgold

        else:
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster_data) #Program memanggil fungsi foundmonster
            if (quit):
                simpan = F12_exitgame.exit()    # Program memanggil fungsi exit
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)  # Program memanggil fungsi save
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)  # Program memanggil fungsi createdragonborn

    elif command == "shopping":
        currentUser = F06_shopping.shop(currentUser, item_data) # Program memanggil fungsi shopping

    elif command == "alduskuy":
        foundmonster = False
        foundmonster, monster = F08_alduskuy.alduskuy(foundmonster) # Program memanggil fungsi alduskuy
        if (foundmonster):
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster) # Program memanggil fungsi foundmonster
            if (quit):
                simpan = F12_exitgame.exit()    # Program memanggil fungsi exit
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)  # Program memanggil fungsi save

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)  # Program memanggil fungsi createdragonborn

    elif command == "switch city":
        foundmonster = False
        currentUser, foundmonster = F09_switchcity.switchcity(currentUser, foundmonster)    # Program memanggil fungsi switchcity
        if(foundmonster):
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster_data)    # Program memanggil fungsi foundmonster
            if (quit):
                simpan = F12_exitgame.exit()    # Program memanggil fungsi exit
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)  # Program memamnggil fungsi save
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)  # Program memanggil fungsi createdragonborn

    elif command == "help":
        section = 0
        F10_help.help(section)  # Program memanggil fungsi help
        
    elif command == "list sidequest":
        monster_data, foundmonster = F14_sidequest.sidequest(sidequest_data,currentUser)    # Program memanggil fungsi sidequest
        if (foundmonster):
            currentUser, quit, create = F04_foundmonster.foundmonster(currentUser, monster_data)    # Program memanggil fungsi foundmonster
            # program melakukan looping berdasarkan monster_data untuk menaikan level sidequest apabila menang
            if (not quit):
                for i in monster_data:
                    if i[0] != "ID":
                        if i[0] == "1":
                            levelup1 = int(currentUser[11]) + 1
                            if levelup1 > 3:
                                currentUser[11] = "3"
                            else:
                                currentUser[11] = str(levelup1)
                        else:
                            levelup2 = int(currentUser[13]) + 1
                            if levelup2 > 3:
                                currentUser[13] = "3"
                            else:
                                currentUser[13] = str(levelup2)

            elif (quit):
                simpan = F12_exitgame.exit()    # Program memanggil fungsi exit
                if (simpan):
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)  # Program memamnggil fungsi save
                print("Thanks for playing skuyrim, goodbye!")
                endprogram = True

            elif (create):
                dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)  # Program memanggil fungsi createdragonborn

    elif command == "save":
        data = [dragonborn_data, item_data, sidequest_data]
        names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
        F11_saveandloadgame.save(data, names, currentUser)  # Program memamnggil fungsi save

    elif command == "exit":
        simpan = F12_exitgame.exit()    # Program memanggil fungsi exit
        if (simpan):
            data = [dragonborn_data, item_data, sidequest_data]
            names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
            F11_saveandloadgame.save(data, names, currentUser)  # Program memamnggil fungsi save

        print("Thanks for playing skuyrim, goodbye!")
        endprogram = True