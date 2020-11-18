import csv,modules

def load(): # Fungsi untuk melakukan load data dragonborn, item, dan sidequest ke dalam variabel dragonborn_data,item_data, sidequest_data
    dragonborn_data = loadfile("data/dragonborn.csv")
    item_data       = loadfile("data/item.csv")
    sidequest_data  = loadfile("data/sidequest.csv")

    return dragonborn_data, item_data, sidequest_data

def loadmonster(): # Fungsi untuk melakukan load data monster ke dalam variabel monster_data
    monster_data    = loadfile("data/monster.csv") 

    return monster_data

def loadfile(x):
    # Membuka file dari hasil input nama file pada fungsi load dan loadmonster menggunakan metode csv.reader untuk menulis
    with open(x) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]

    return data

def dataload(dragonborn_data, currentUser):
    dummy = [" $NOUSER", "$NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"," $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]
    # Melakukan looping berdasarkan array dragonborn_data
    for i in (dragonborn_data):
        if i[1] != 'Nama':
            print(str(i[1])+" - lvl "+i[4]) # Menampilkan nama karakter dan level karakter yang sudah ada tersimpan dalam file dragonborn.csv

    command = str(input("$ ")).capitalize() # Pemain memberikan input aksi yang ingin dilakukan apakah load atau membuat karaktaker. Jika load maka memberikan input dari nama karakter. Jkia membuat karakter memberikan input create
    # Melakukan looping berdasarkan array dragonborn_data
    for i in (dragonborn_data):
        if i[1] == command: # Apabila pemain memberikan input nama untuk melakukan load
            newChar = False
            currentUser = i
            print("Welcome back to the world of Skuyrim "+currentUser[1]+"!")
            return newChar, currentUser
    if command == "Create": # Apabila pemain memberikan input create untuk membuat karakter
        newChar = True
        return newChar, dummy

def save(data, names, currentUser):
    folderDirectory = "data/"
    # Melakukan looping berdasarkan panjang array names
    for i in range(modules.panjang(names)):
        name = str(folderDirectory + names[i])
        writeFile(name, data[i])    
    print("Your progress on character", currentUser[1], "has been saved")

def writeFile(namaFile, arrayData):
    # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis
    with open(namaFile, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in arrayData:
            writer.writerow(row)
