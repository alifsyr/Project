# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import csv
import F11_savegameandloadgame
import F12_exitgame
from F11_savegameandloadgame import loadfile
import random
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
        simpan = F12_exitgame.exit()
        if (simpan):
            data = [dragonborn_data, item_data, monster_data, sidequest_data]
            names = ["Dragonborn.csv", "Item.csv",
                     "Monster.csv", "Sidequest.csv"]
            F11_savegameandloadgame.save(data, names)
        endprogram = True

# DUMMY ARRAY FOR CURRENT USER


def dummy_array():  # Harusnya pake login lebih efektif, karena kita tinggal
    load(dragonborn_data)  # masukin data user sesuai nama character yang sudah
    dummy_arr = []  # ada di dragonbron.csv
    rows = 0

    for row in reader:
        dummy_arr.append(row)
        rows = rows + 1

    return dummy_arr


class final_boss:            #Untuk membuat object(Final boss= "Alduskuy"), digunakan fungsi class. di F08 saya sudah membuat final_bossnya dengan ketentuan tertentu
    def __init__(self, Attack, Defense, HP):
        self.Attlow = -17
        self.Atthigh = +100
        self.MaxHP = HP
        self.Def = Defense
        self.HP = HP

    def gen_dmg(self):
        return random.randrange(self.Attlow, self.Atthigh)
