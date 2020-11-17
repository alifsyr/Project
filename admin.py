import modules, F11_saveandloadgame, F12_exitgame

dragonborn_data, item_data, sidequest_data = F11_saveandloadgame.load()
monster_data = F11_saveandloadgame.loadmonster()
endprogram = False

while (not endprogram):
    data = []
    password = (input("Enter password: "))
    if password == 'akusukakamu':
        print("Welcome!")
        print("What database do you want to user? (1 - item, 2 - monster)")
        database = int(input("database: ")) #awal lgsg muncul ini
        modules.printdata(item_data, monster_data, database, data)
    
        while (not endprogram):
            data = []
            command = str(input("$ "))
            if command == "switch":
                print("What database do you want to user? (1 - item, 2 - monster)")
                database = int(input("database: "))
                modules.printdata(item_data,monster_data,database,data)

            elif command == "add":
                item_name = str(input("item name: "))
                item_atk = str(input("item atk: "))
                item_def = str(input("item deff: "))
                item_luck = str(input("item luck: "))
                item_health = str(input("item health: "))
                item_magic = str(input("item magic: "))
                item_gold = str(input("item gold: "))
                item_region = str(input("item region(1 for windhelm, 2 for solitude): "))
                item_data += [[str(modules.generateid(item_data)),item_name,item_atk,item_magic,item_def,item_luck,item_health,item_region,item_gold]] #masukin ke array sementara (magic sm price ga ada di spesifikasi)
                print("data successfully added to database")

            elif command == "delete":
                data = modules.printdata(item_data, monster_data, 1, data)
                delete = input("Which number: ")
                update_arr = [['ID','Nama','Attack','Magic','Defense','Luck','HP','City','Price']]
                for i in data:
                    if i[0] != delete:
                        update_arr +=[i]
                    elif i[0] == delete:
                        print("Successfully deleted item "+i[1])
                item_data = update_arr
                data = []
                modules.printdata(item_data,monster_data,1,data)
                

            elif command == "save":
                currentUser = ["0","Admin"]
                data = [dragonborn_data, item_data, monster_data, sidequest_data]
                names = ["dragonborn.csv", "item.csv", "monster.csv", "sidequest.csv"]
                F11_saveandloadgame.save(data, names, currentUser)

            elif command == "exit":
                simpan = F12_exitgame.exit()
                if (simpan):
                    currentUser = ["0","Admin"]
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                exit()
    else:
        print("Password salah!")
