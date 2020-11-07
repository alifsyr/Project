def createdragonborn(dragonborn_data,currentUser):
    nama = str(input("Masukan nama character: ")).capitalize()
    print(nama,"created")
    print("Welcome "+nama+" to the world of Skuyrim!")
    print("Choose one faction: ")
    print("1. Empire (+ 1 attack)")
    print("2. Stormcloaks (+ 1 magic)")
    faction = int(input("Masukkan nomor faction diatas(1/2): "))
    while True:
        if faction == 1:
            newchar = [str(generateid(dragonborn_data)),nama,'100','100','1','6','5','5','0','0','null']
            dragonborn_data += [newchar]
            currentUser = newchar
            break
        elif faction == 2:
            newchar = [str(generateid(dragonborn_data)),nama,'100','100','1','5','6','5','0','0','null']
            dragonborn_data += [newchar]
            currentUser = newchar
            break
        else :
            print("Nomor yang anda masukkan tidak sesuai!")
            faction = int(input("Masukkan nomor faction diatas (1/2): "))

    return dragonborn_data, currentUser

def generateid(dragonborn_data):
    for i in (dragonborn_data):
        if i[0] != "ID":
            maks = 0
            if int(i[0]) > maks:
                maks = int(i[0])
    ID = maks + 1
    return ID