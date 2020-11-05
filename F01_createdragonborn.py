import csv
def createdragonborn(dragonborn_data,currentUser):
    print ("$ create newChar")
    nama = input("Nama Dragonborn: ")
    i=0
    print("newChar created")
    print("Welcome "+str(nama)+" to the world of Skuyrim!")
    print("Choose one faction: ")
    print("1. Empire (+ 1 atatck)")
    print("2. Stormcloaks (+ 1 magic)")
    faction = int(input("Masukkan nomor faction diatas(1/2: "))
    while True:
        if faction == 1:
            newchar = [str(i), str(nama), '100', '100', '1', '6', '5', '5', '0', 'null']
            dragonborn_data += [newchar]
            currentUser = newchar
            break
        elif faction == 2:
            newchar = [str(i), str(nama), '100', '100', '1', '5', '6', '5', '0', 'null']
            dragonborn_data += [newchar]
            currentUser = newchar
            break
        else :
            print("Nomor yang anda masukkan tidak sesuai!")
            faction = int(input("Masukkan nomor faction diatas (1/2): "))

    return dragonborn_data, currentUser
