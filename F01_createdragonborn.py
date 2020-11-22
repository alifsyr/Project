import modules

def createdragonborn(dragonborn_data,currentUser):
    nama = str(input("Masukan nama character: \n$ ")).capitalize()
    print(nama,"created")
    print("Welcome "+nama+" to the world of Skuyrim!")
    print("Choose one faction: \n1. Empire (+ 1 attack) \n2. Stromcloacks (+ 1 magic)")

    result = int(input("Masukkan nomor faction diatas(1/2): \n$ "))
    if result == 1:
        print("Choose one city: \n1. Windhelm \n2. solitude")
        city = choosecity(int(input("Masukkan nomor city diatas(1/2): \n$ ")))
        newchar = [str(modules.generateid(dragonborn_data)),nama,'100','100','1','6','5','5','0','0',str(city),'1','100','1']
        dragonborn_data += [newchar]
        currentUser = newchar

    elif result == 2:
        print("Choose one city: \n1. Windhelm \n2. solitude")
        city = choosecity(int(input("Masukkan nomor city diatas(1/2): \n$ ")))
        newchar = [str(modules.generateid(dragonborn_data)),nama,'100','100','1','5','6','5','0','0',str(city),'1','100','1']
        dragonborn_data += [newchar]
        currentUser = newchar
    
    print("Welcome back to the world of Skuyrim "+currentUser[1]+"!")

    return dragonborn_data,currentUser

def choosecity(x):
    if x == 1:
        return x
    
    elif x == 2:
        return x