def sidequest(sidequest_data,currentUser):
    sidequest_arr = []
    monster_data  = []
    foundmonster  = False
    print("List of all available sidequests:")
    # Melakukan looping berdasarkan array sidequest_data
    for i in sidequest_data:
        if i[0] != "ID":
            if  currentUser[11] == i[1] and i[0] == "1":
                sidequest_arr +=[[i[0],i[2],i[3]]]
                print(i[0]+".",i[2],"- kill",i[3])
            elif currentUser[13] == i[1] and i[0] == "2":
                sidequest_arr +=[[i[0],i[2],i[3]]]
                print(i[0]+".",i[2],"- kill",i[3])
    result = input("What do you want to do? (type cancel to cancel)\n$ ")   # Pemain memebrikan input nomor sidequest atau cancel
    while result != "cancel":   # Selama pemain tidak memberikan input cancel
        # Melakukan looping berdasarkan array sidequest_arr
        for i in sidequest_arr:
            if result == i[0]: # Jika nomor yang diberikan sesuai dengan list sidequest
                monster_data = i[2] # Memasukan nama monster kedalam variabel monster data
        # Melakukan looping berdasarkan array sidequest_data
        for i in sidequest_data:
            if i[0] != 'ID':
                if monster_data == i[3]: # Jika nama monster yang dipilih sesuai dengan data pada array sidequest_data
                    monster_data = [["ID", "Nama", "Attack", "Defense", "Health"],[i[0],i[3],i[4],i[5],i[6]]] # Variabel monster_data menjadi array of array of string yang berisi data monster yang dipilih
        foundmonster = True
        return monster_data, foundmonster
    
    print("Your sidequest have been canceled")  # Jika input dari pemain adalah cancel menampilkan pesan cancel
    return monster_data, foundmonster 