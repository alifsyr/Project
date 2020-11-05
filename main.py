# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import F01_createdragonborn,F06_Shopping,F08_alduskuy,F11_savegameandloadgame,F12_exitgame

'''
Zachrandika Alif Syahreza
Dimas Farhan Anshari
Ali Zayn Murteza
'''


# KAMUS GLOBAL
'''
    dragonborn_data : array of array of string
    item_data       : array of array of string
    monster_data    : array of array of string
    sidequest_data  : array of array of string
'''

endprogram = False
currentUser = [" $NOUSER", " %NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]

while (not endprogram):
    print("Welcome to Skuyrim")
    dragonborn_data, item_data, monster_data, sidequest_data = F11_savegameandloadgame.load()

    command = str(input("$ "))
    if command == "create newChar":
        dragonborn_data, currentuser = F01_createdragonborn.createdragonborn(dragonborn_data, currentUser)

    elif command == "exit":
        simpan = F12_exitgame.exit()
        if (simpan):
            data = [dragonborn_data, item_data, monster_data, sidequest_data]
            names = ["Dragonborn.csv", "Item.csv","Monster.csv", "Sidequest.csv"]
            F11_savegameandloadgame.save(data, names)
        endprogram = True

