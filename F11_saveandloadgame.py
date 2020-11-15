import csv

def load():
    dragonborn_data = loadfile("data/dragonborn.csv")
    item_data       = loadfile("data/item.csv")
    sidequest_data  = loadfile("data/sidequest.csv")

    return dragonborn_data, item_data, sidequest_data

def loadmonster():
    monster_data    = loadfile("data/monster.csv")

    return monster_data

def loadfile(x):
    with open(x) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = [row for row in reader]

    return data

def dataload(dragonborn_data, currentUser):
    dummy = [" $NOUSER", "$NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"" $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]
    for i in (dragonborn_data):
        if i[1] != 'Nama':
            print(str(i[1])+" - lvl "+i[4])

    command = str(input("$ ")).capitalize()
    for i in (dragonborn_data):
        if i[1] == command:
            newChar = False
            currentUser = i
            print("Welcome back to the world of Skuyrim "+currentUser[1]+"!")
            return newChar, currentUser
    if command == "Create":
        newChar = True
        return newChar, dummy

def save(data, names, currentUser):
    import modules
    folderDirectory = "data/"
    # Melakukan looping berdasarkan panjang array names
    for i in range(modules.panjang(names)):
        name = str(folderDirectory + names[i])
        writeFile(name, data[i])    
    print('Your progress on character', currentUser[1], 'has been saved')

def saveadmin(data, names):
    import modules
    folderDirectory = "data/"
    # Melakukan looping berdasarkan panjang array names
    for i in range(modules.panjang(names)):
        name = str(folderDirectory + names[i])
        writeFile(name, data[i])    
    print('All changes have been saved')

def writeFile(namaFile, arrayData):
    # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis
    with open(namaFile, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in arrayData:
            writer.writerow(row)
