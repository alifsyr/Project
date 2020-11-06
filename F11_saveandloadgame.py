import csv

def load():
    dragonborn_data        = loadfile("data/Dragonborn.csv")
    item_data              = loadfile("data/Item.csv")
    monster_data           = loadfile("data/Monster.csv")
    sidequest_data         = loadfile("data/Sidequest.csv")
    
    return dragonborn_data, item_data, monster_data, sidequest_data

def loadfile(x):
    with open(x) as csvfile:
        reader = csv.reader (csvfile,delimiter=',')
        data   = [row for row in reader]
    
    return data

def dataload(dragonborn_data,currentUser):
    dummy = [" $NOUSER", "$NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER", " $NOUSER"]
    for i in (dragonborn_data):
        if i[1] != 'Nama':
            print(str(i[1])+" - lvl "+i[4])

    command = input("$ ")
    for i in (dragonborn_data):
        if i[1] == command:
            newChar = False
            currentUser = i
            print("Welcome back to the world of Skuyrim "+currentUser[1]+"!")
            return newChar, currentUser
    if command == "create newChar":
        newChar = True
        return newChar, dummy


def save(data, names,currentUser):
    import modules
    folderDirectory = "data/"
    for i in range(modules.panjang(names)):     # Melakukan looping berdasarkan panjang array names
        name = str(folderDirectory + names[i])     # input nama file csv
        writeFile(name, data[i])    # Memanggil fungsi writeFile
    print('Your progress on character', str(currentUser[1]) ,'has been saved')
    
def writeFile(namaFile, arrayData):
    
    with open(namaFile, mode='w',newline='') as csvfile:      # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis 
        writer = csv.writer(csvfile)
        for row in arrayData:
            writer.writerow(row)