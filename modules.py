import random

def panjang(x):
    len = 0
    for i in x:
        len  = len + 1
    return(len)  

def randomchoice(x):
    choice = random.choice(x)
    return choice

def randomrange(x):

    choice = random.randrange(1,x)
    return choice

def generateid(x):
    for i in (x):
        if i[0] != "ID":
            maks = 0
            if int(i[0]) > maks:
                maks = int(i[0])
    ID = maks + 1
    return ID

def printdata(item_data, monster_data, database, data):
    sum = 1
    if database == 1:
        print("Showing data of all item:")
        for i in item_data: #display data item
            if i[1] != "Nama":
                data += [[str(sum),i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]]
                sum += 1
        print("{:<8} {:<30} {:<8} {:<8} {:<8} {:<8} {:<8} {:<5} {:<8}".format('No','Nama','Attack','Magic','Defense','Luck','HP','City','Price'))
        for i in data:
            No,Nama,Attack,Magic,Defense,Luck,HP,City,Price = i
            print("{:<8} {:<30} {:<8} {:<8} {:<8} {:<8} {:<8} {:<5} {:<8}".format(No,Nama,Attack,Magic,Defense,Luck,HP,City,Price))
    elif database == 2:     #displaymonster
        print("Showing data of all monster:")
        for i in monster_data:
            if i[1]!= 'Nama':
                data += [[str(sum),i[1],i[2],i[3],i[4]]]
                sum += 1
        print("{:<8} {:<30} {:<8} {:<8} {:<8}".format('No','Nama','Attack','Defense','HP'))
        for i in data:
            No,Nama,Attack,Defense,HP = i
            print("{:<8} {:<30} {:<8} {:<8} {:<8}".format(No,Nama,Attack,Defense,HP))

    return data
