import modules, F11_saveandloadgame, F12_exitgame

dragonborn_data, item_data, sidequest_data = F11_saveandloadgame.load() # melakukan load file dragonborn.csv, item.csv, sidequest,csv
monster_data = F11_saveandloadgame.loadmonster() # melakukan load file monster.csv
endprogram = False

while (not endprogram):
    data = []
    password = (input("Enter password: "))  # Pemain memasukan input password
    if password == 'akusukakamu':   # Jika password benar
        print("Welcome!")
        print("What database do you want to user? (1 - item, 2 - monster)")
        database = int(input("database: ")) # Pemain memilih database yang ingin ditampilkan
        modules.printdata(item_data, monster_data, database, data)  # Progam menampilkan database sesuai input yang diberikan

        while (not endprogram):
            data = []
            command = str(input("$ "))  # Pemain memberikan input aksi yang ingin dilakukan
            if   command == "switch":   # Jika pemain memberikan input switch
                print("What database do you want to user? (1 - item, 2 - monster)")
                database = int(input("database: ")) # Pemain memilih database yang ingin ditampilkan
                modules.printdata(item_data,monster_data,database,data) # Progam menampilkan database sesuai input yang diberikan

            elif command == "add":  # Jika pemain memberikan input add maka program akan melakukan penambahan pada database item
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

            elif command == "delete": # Jika pemain memberikan input delete maka program akan melakukan penghapusan pada database item
                data = modules.printdata(item_data, monster_data, 1, data)
                delete = input("Which number: ") # Pemain memberikan input nomor data item yang akan dihapus
                update_arr = [['ID','Nama','Attack','Magic','Defense','Luck','HP','City','Price']]
                # Melakukan looping berdasarkan array data
                for i in data:
                    if i[0] != delete:  # Program melakukan validasi terhadap data yang dihapus, sehingga data yang dihapus dibuang
                        update_arr +=[i]
                    elif i[0] == delete:    # Program melakukan validasi terhadap data yang dihapus, apabila berhasil maka akan menampilkan pesan sukses
                        print("Successfully deleted item "+i[1])
                item_data = update_arr
                data = []
                modules.printdata(item_data,monster_data,1,data) # Program menampilkan database item setelah dilakukan penghapusan

            elif command == "save": # Jika pemain memberikan input save maka program akan melakukan penyimpanan pada file yang terdapat dalam array names
                currentUser = ["0","Admin"]
                data = [dragonborn_data, item_data, monster_data, sidequest_data]
                names = ["dragonborn.csv", "item.csv", "monster.csv", "sidequest.csv"]
                F11_saveandloadgame.save(data, names, currentUser) # Memanggil program untuk melakukan save

            elif command == "exit": # Jika pemain memberikan input exit maka program akan keluar dengan menanyakan apakah data ingin disimpan atau tidak
                simpan = F12_exitgame.exit() # Memanggil program untuk exit
                if (simpan):    # Apabila pemain ingin melakukan penyimpanan data ketika ingin exit
                    currentUser = ["0","Admin"]
                    data = [dragonborn_data, item_data, sidequest_data]
                    names = ["dragonborn.csv", "item.csv", "sidequest.csv"]
                    F11_saveandloadgame.save(data, names, currentUser)
                exit()

    else:   # Jika password salah
        print("Password salah!")
