def createdragonborn():
    print ("$ create newChar")
    nama = input("Nama Dragonborn: ")
    i=0
    while True:
        if dragonborn[i] == '*':
            dragonborn[i] = [str(i), str(nama), '100', '100', '1', '5', '5', '5', '0', 'null']
            break
        else:
            i+=1
    print("newChar created")
    print("Welcome "+str(nama)+" to the world of Skuyrim!"
    print("Choose one faction: ")
    print("1. Empire (+ 1 atatck)")
    print("2. Stormcloaks (+ 1 magic)")
    while True:
        faction = int(input("Masukkan nomor faction diatas(1/2: "))
        if faction == 1:
            dragonborn[i] = [str(i), str(nama), '100', '100', '1', '6', '5', '5', '0', 'null']
            break
        elif faction == 2:
            dragonborn[i] = [str(i), str(nama), '100', '100', '1', '5', '6', '5', '0', 'null']
            break
        else :
            print("Nomor yang anda masukkan tidak sesuai!")
            faction = int(input("Masukkan nomor faction diatas (1/2): "))