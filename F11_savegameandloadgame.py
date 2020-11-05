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

def save(data, names):
    import modules
    folderDirectory = "data/"
    for i in range(modules.panjang(names)):     # Melakukan looping berdasarkan panjang array names
        name = str(folderDirectory + names)     # input nama file csv
        writeFile(name, data[i])    # Memanggil fungsi writeFile
    print('Data berhasil disimpan!')
    
def writeFile(namaFile, arrayData):
    
    with open(namaFile, mode='w',newline='') as csvfile:      # Membuka file dari hasil input name pada fungsi save dengan fungsi open dan menggunakan metode w untuk menulis 
        writer = csv.writer(csvfile)
        for row in arrayData:
            writer.writerow(row)