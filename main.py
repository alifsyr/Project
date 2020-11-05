# Tugas Besar IF1210 Dasar pemrograman
# Kelompok Stormcloak

import csv
import F01_createdragonborn,F04_monsterbattleandexplore,F06_Shopping,F08_alduskuy,F11_savegameandloadgame,F12_exitgame
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

# DUMMY ARRAY FOR CURRENT USER


def dummy_array():  # Harusnya pake login lebih efektif, karena kita tinggal
    load(dragonborn_data)  # masukin data user sesuai nama character yang sudah
    dummy_arr = []  # ada di dragonbron.csv
    rows = 0

    for row in reader:
        dummy_arr.append(row)
        rows = rows + 1

    return dummy_arr


# Untuk membuat object(Final boss= "Alduskuy"), digunakan fungsi class. di F08 saya sudah membuat final_bossnya dengan ketentuan tertentu
class final_boss:
    def __init__(self, Attack, Defense, BOSS_HP):
        self.Attlow = -30
        self.Atthigh = +70
        self.MaxHP = BOSS_HP
        self.Def = Defense
        self.HP = BOSS_HP

    def gen_dmg(self):
        return random.randrange(self.Attlow, self.Atthigh)

    def hp_boss(self):
        return self.HP

    def dmg_taken(self, dmg):
        self.HP = self.HP - dmg
        if ((self.HP) <= 0):
            self.HP = 0
        return self.HP
