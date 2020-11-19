import modules, F10_help

def foundmonster(currentUser, monster_data):
    #bagian dari fungsi yang ngeset karakter bertemu monster (jenisnya dan speknya)
    endfight = False
    data = []
    for i in monster_data: #skema membuat range data monster yang ada
        if i[0] != "ID":
            data = data + [i]
    monster = modules.randomchoice(data) #mencari monster dengan cara randomize data ID monster

    while (not endfight):
        quit = False
        newChar = False

        print("You have met a "+ monster[1] +", will you fight or will you flee ?\n"+monster[1]+" stats: \nAttack:",monster[2] ,"\nDefense:", monster[3],"\nHealth:", monster[4])
        result = str(input("$ ")) #masukan aksi dari user

        if result == "fight":  # apabila masukan = "fight" maka akan melawan monster
            currentUser , quit, newChar, endfight = fight(monster, currentUser, endfight, quit, newChar)

            return currentUser, quit, newChar
        
        elif result == "flee": #apabila masukan = "flee" maka akan terjadi randomize kejadian yang bersangkutan dengan luck
            result = modules.randomrange(501) # terpilih satu angka dari range 0 - 500
            if result >= (500 - int(currentUser[8])): #apabila result >= angka 500 - luck maka berhasil kabur

                return currentUser, quit, newChar
           
            else: #jika tidak maka akan melawan monster
                print("Bad luck ! You can't run from the monster")
                currentUser , quit, newChar, endfight = fight(monster, currentUser, endfight, quit, newChar)

                return currentUser, quit, newChar

def fight(monster, currentUser, endfight, quit, newChar):
    # bagian dari fungsi yang membuat skenario fight / melawan mosnter
    # atribut yang dipakai: - karakter (Nama, HP, Defense, Strike (Attack), Magic)
    #                                   - monster (Nama, HP, Defense, Attack)
    #Fight bersifat sequencial yang artinya pilihan dari aksi berkurang terus hingga tipe aksi attack habis
    while (not endfight):
        print("What action will you take?\n1. strike - "+ currentUser[5] +"\n2. magic - "+ currentUser[6] +"\n3. flee")
        result = str(input("$ ")) # user input aksi yang mau dilakukan
        if result == "strike": #memilih tipe attack "strike"
            if int(monster[3]) > 0: #monser memiliki defense
                dmg = int(monster[3]) - int(currentUser[5])
                monster[3] = str(dmg)

                if dmg < 0: 
                    dmg = -dmg
                    HP = int(monster[4]) - dmg # berapa banyak attack "Strike" karakter yang mengenai monster tatapi teredam defense monster
                    monster[4] = str(HP)
                    if int(monster[4]) <= 0: #defense monster break serta mengurangi darah hingga 0 atau kurang dari 0
                        print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)

                    else: # defense monster break tetapi tidak membuat HP monster menjadi 0
                        monster[3] = "0"
                        print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                else: # defense mosnter melindunngi monster 
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)
            
            else: # monster tidak mempunyai Defense

                if int(monster[4]) <= 0: 
                    print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                    currentUser = win(currentUser, monster)
                    quit = False
                    newChar = False
                    endfight = True

                else: #monster menerima damage 
                    monsterHP = int(monster[4]) - int(currentUser[5])

                    if monsterHP > 0: # darah monster masih ada
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[5] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                    else: # darah monster 0 atau kurang dari 0
                        print(monster[1],"took",currentUser[5],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)
        
        elif result == "magic": # karakter menyerang dengan tipe serangan "Magic"

            if int(monster[3]) > 0: # defense monter > 0
                dmg = int(monster[3]) - int(currentUser[6])
                monster[3] = str(dmg)

                if dmg < 0: 
                    dmg = -dmg
                    HP = int(monster[4]) - dmg # berapa banyak attack "Magic" karakter yang mengenai monster tatapi teredam defense monster
                    monster[4] = str(HP)
                    if int(monster[4]) <= 0: # magic menembus defense monster dan mengurangi darah hingga 0
                        print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)

                    else: # magic menembus defense monster tetapi darah monster tidak 0 atau kurang dari 0
                        monster[3] = "0"
                        print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                else: # defense monter melindungi monster
                    print(monster[1],"took 0 dmg")
                    newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)
            
            else: #monster tidak punya defense

                if int(monster[4]) <= 0:
                    print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                    currentUser, newChar, quit, endfight = win(currentUser, monster)

                else:
                    monsterHP = int(monster[4]) - int(currentUser[6]) # darah monster yang tersisa

                    if monsterHP > 0: #monster menerima damage dan darah lebih dari 0
                        monster[4] = str(monsterHP)
                        print(monster[1]+" took "+ currentUser[6] +" dmg and health dropped to "+ monster[4])
                        newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

                    else: #monster menerima damage dan darah kurang dari sama dengan 0
                        print(monster[1],"took",currentUser[6],"dmg and health dropped to 0")
                        currentUser, newChar, quit, endfight = win(currentUser, monster)
        
        elif result == "help": #memilih list2 yang tersedia
            section = 1
            F10_help.help(section)

        elif result == "flee": #memilih untuk flee (prosedur sama seperti di randomize def foundmonster (currentUser, monster_data))
            result = modules.randomrange(501)
            if result >= (500 - int(currentUser[8])):
                quit = False
                newChar = False
                endfight = True

            else:
                print("Bad luck ! You can't run from the monster")
                newChar, quit, currentUser, endfight = fightback(monster, currentUser, quit, newChar,endfight)

    return currentUser , quit, newChar, endfight

def fightback(monster,currentUser,quit,newChar,endfight):
    # monster sudah diserang secara sequential tetapi tidak mati
    # monster menyerang balik
    # atribut yang dipakai: - karakter (Nama, HP, Defense)
    #                                   - monster (Nama,  Attack)
    if int(currentUser[7]) > 0: # defense karakter > 0
        dmg = int(currentUser[7]) - int(monster[2]) #damage monster yang teredam defense
        currentUser[7] = str(dmg)

        if dmg < 0:
            dmg = -dmg
            HP = int(currentUser[3]) - dmg #berapa banyak damage yang diimplikasikan monster kepada karakter
            currentUser[3] = str(HP)
            if int(currentUser[3]) <= 0: # attack monster menembus defens edan mengurangi darah karakter hingga kurang dari sama dengan 0
                print(monster[1],"strike for "+ str(dmg) +" dmg")
                currentUser[3] = "0"
                print("Game over!\nYour character is dead.\nYou can create a new character or exit game.")
                result = str(input("$ ")) #mendapat opsi quit game atau create new character

                if result == "create": # user memilih opsi create
                    newChar = True
                    quit = False
                    endfight = True

                    return newChar, quit, currentUser , endfight

                elif result == "exit": # user memilih opsi exit game
                    newChar = False
                    quit = True
                    endfight = True

                    return newChar, quit, currentUser , endfight
            
            else: # darah karakter tidak kurang dari sama dengan 0
                currentUser[7] = "0"
                print(monster[1],"strike for "+ str(dmg) +" dmg")
                newChar = False
                quit = False
                endfight = False

                return newChar, quit, currentUser, endfight

        else: #defense melindungi karakter
            print(monster[1],"strike for 0 dmg")
            quit = False
            newChar = False
            endfight = False

            return newChar, quit, currentUser, endfight

    else: # karakter tidak memiliki defense

        if int(currentUser[3]) <= 0: # karakter menerima damage dan mati (prosedur sama dengan fungsi karakter kalah sebelumnya)
            print(monster[1],"strike for "+ str(monster[2]) +" dmg")
            currentUser[3] = "0"
            print("Game over!\nYour character is die.\nYou can create a new character or exit game.")
            result = str(input("$ "))

            if result == "create":
                newChar = True
                quit = False
                endfight = True

                return newChar, quit, currentUser , endfight

            elif result == "exit":
                newChar = False
                quit = True
                endfight = True

                return newChar, quit, currentUser , endfight

        else: # karakter menerima dammage tetapi tidak mati (health / HP tidak kurang dari sama dengan 0)
            HP = int(currentUser[3]) - int(monster[2])
            currentUser[3] = str(HP)
            newChar, quit, currentUser, endfight = shieldbroken(currentUser,monster,HP,quit,newChar)

    return newChar, quit, currentUser, endfight

def shieldbroken(currentUser,monster,HP,quit,newChar):
    # bagian fungsi ini membuat kejadian dimana defense karkater atau keduanya pecah / kurang dari sama dengan 0
    # atribut yang dipakai: - karakter (Nama, HP,)
    #                                   - monster (Nama,  Attack)
    if int(currentUser[3]) > 0:  # kejadian dimana karakter memiliki health > 0
        currentUser[3] = str(HP)
        print(monster[1],"strike for "+ str(monster[2]) +" dmg")
        newChar = False
        quit = False
        endfight = False

        return newChar, quit, currentUser, endfight

    else: # kajadian dimana karakter tidak memiliki HP atau HP <= 0
        print(monster[1],"strike for "+ str(monster[2]) +" dmg")
        currentUser[3] = "0"
        print("Game over!\nYour character is die.\nYou can create a new character or exit game.")
        result = str(input("$ ")) # mendapat opsi membuat karakter baru atau exit game

        if result == "create": # user memilih membuat karakter baru
            newChar = True
            quit = False
            endfight = True

            return newChar, quit, currentUser , endfight
        
        elif result == "exit": # user memilih exit game
            newChar = False
            quit = True
            endfight = True

            return newChar, quit, currentUser , endfight

def win(currentUser, monster):
    # bagian fungsi ini membuat kejadian karakter memenangkan pertarungan 
    if monster[1] == "Alduskuy": #karakter menang melawan final bos
        print("You have won the fight! \nGot 10000 gold \nExperience + 1000")
        gold = int(currentUser[12]) + 10000
        exp  = int(currentUser[9]) + 1000
        currentUser[12] = str(gold)
        currentUser[9] = str(exp)
        print("Do you want to create a new character or exit?")
        result = str(input("$ ")) # setelah melawan final bos dan menang mendapat opsi membuat karakter baru atau exit  game

        if result == "create": # user memilih create new character
            newChar = True
            quit = False
            endfight = True

            return currentUser, newChar, quit, endfight

        elif result == "exit": #user memilih exit game
            newChar = False
            quit = True
            endfight = True

            return currentUser, newChar, quit, endfight

    else: # karakter menang melawan monster biasa
        print("You have won the fight! \nGot 10 gold \nExperience + 50")
        gold = int(currentUser[12]) + 10
        exp  = int(currentUser[9]) + 50
        currentUser[9] = str(exp)
        currentUser[12] = str(gold)
        newChar = False
        quit = False
        endfight = True

        return currentUser, newChar, quit, endfight



