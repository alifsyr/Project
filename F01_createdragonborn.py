import modules

def createdragonborn(dragonborn_data,currentUser):
    nama = str(input("Masukan nama character: \n$ ")).capitalize()
    print(nama,"created")
    print("Welcome "+nama+" to the world of Skuyrim!")
    print("Choose one faction: \n1. Empire (+ 1 attack) \n2. Stromcloacks (+ i magis)")

    result = int(input("Masukkan nomor faction diatas(1/2): \n$ "))
    if result == 1:
        print("Choose one city: \n1. Windhelm \n2. solitude")
        city = choosecity(int(input("Masukkan nomor city diatas(1/2): \n$ ")))
        newchar = [str(modules.generateid(dragonborn_data)),nama,'100','100','1','6','5','5','0','0',str(city),'null','100']
        dragonborn_data += [newchar]
        currentUser = newchar

        return dragonborn_data,currentUser

    elif result == 2:
        print("Choose one city: \n1. Windhelm \n2. solitude")
        city = choosecity(int(input("Masukkan nomor city diatas(1/2): \n$ ")))
        newchar = [str(modules.generateid(dragonborn_data)),nama,'100','100','1','5','6','5','0','0',str(city),'null','100']
        dragonborn_data += [newchar]
        currentUser = newchar

        return dragonborn_data,currentUser

def choosecity(x):
    if x == 1:
        return x
    
    elif x == 2:
        return x