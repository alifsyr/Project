# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import F01_createdragonborn, F02_attribute, F06_Shopping, F11_saveandloadgame, F12_exitgame

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

endprogram = False
currentUser = [" $NOUSER", "$NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"" $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]

print("Welcome to Skuyrim")
dragonborn_data, item_data, monster_data, sidequest_data = F11_saveandloadgame.load()

print("Choose your character or create new character :")
newChar, currentUser = F11_saveandloadgame.dataload (dragonborn_data, currentUser)

if (newChar):
    dragonborn_data, currentUser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

while (not endprogram):
    gold = 0
    command = str(input("$ ")).capitalize()

    if command == "Status":
        F02_attribute.attribute(currentUser)

    elif command == "Shopping":
        F06_Shopping.shop(currentUser, item_data)

    elif command == "Save":
        data = [dragonborn_data, item_data, monster_data, sidequest_data]
        names = ["dragonborn.csv", "item.csv", "monster.csv", "sidequest.csv"]
        F11_saveandloadgame.save(data, names, currentUser)

    elif command == "Exit":
        simpan = F12_exitgame.exit()
        if (simpan):
            data = [dragonborn_data, item_data, monster_data, sidequest_data]
            names = ["dragonborn.csv", "item.csv","monster.csv", "sidequest.csv"]
            F11_saveandloadgame.save(data, names, currentUser)
        print("Thanks for playing skuyrim, goodbye!")
        endprogram = True