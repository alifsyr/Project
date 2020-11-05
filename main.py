# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import F11_savegameandloadgame
from F11_savegameandloadgame import loadfile
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

while (not endprogram):
    print("Welcome to Skuyrim")
    dragonborn_data, item_data, monster_data, sidequest_data = F11_savegameandloadgame.load()

    command = str(input("$ "))
    if command == "exit":
                simmpan = F12_exitgame.exit()
                if (simmpan):
                    data = [dragonborn_data, item_data, monster_data, sidequest_data]
                    names = ["Dragonborn.csv", "Item.csv", "Monster.csv", "Sidequest.csv"]
                    F11_savegameandloadgame.save(data, names)
                endprogram = True

# DUMMY ARRAY FOR CURRENT USER


def dummy_array():
    load(dragonborn_data)
    dummy_arr = []
    rows = 0

    for row in reader:
        dummy_arr.append(row)
        rows = rows + 1

    return dummy_arr
