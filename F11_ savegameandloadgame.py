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