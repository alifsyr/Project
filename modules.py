'''
MODULES.PY

panjang             | 10 
intSort             | 21
strSort             | 44
eOrde               | 81
'''

def panjang(x):
    len = 0
    for i in x:
        len  = len + 1
    return(len)  
'''
database        : array, urutkan array ini
column          : int, berdasarkan kolom ini
order           : string, 'ascending' atau 'descending'
'''

def intSort(database, column, order):
    for i in range(panjang(database)):
        # Mengurutkan data berdasarkan kolom berisi integer
        if (i > 0):
            current = i
            selected = i-1
            
            if (order == "ascending"):
                while (int(database[current][column]) < int(database[selected][column]) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1
            else:
               while (int(database[current][column]) > int(database[selected][column]) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1 
    return database

def strSort(database, column, order):
    for i in range(panjang(database)):
        # Mengurutkan data berdasarkan kolom berisi integer
        if (i > 0):
            current = i
            selected = i-1
            
            if (order == "ascending"):
                while ((stringOrder(database[current][column], database[selected][column])) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1
            else:
               while ((stringOrder(database[current][column], database[selected][column])) and selected>=0):
                    temp = database[selected]
                    database[selected] = database[current]
                    database[current] = temp
                    selected -= 1
                    current -= 1 
    return database

def stringOrder(stringA, stringB):
    lenA = panjang(stringA)
    lenB = panjang(stringB)
    if lenA < lenB:
        length = lenA
    else:
        length = lenB

    i = 0
    for i in range(length):
        if eOrde(stringA[i]) != eOrde(stringB[i]):
            return eOrde(stringA[i]) < eOrde(stringB[i])
    return lenA < lenB

def eOrde(char):
    '''
    ASCII for integer       : 48-57
    ASCII for uppercase     : 65-90
    ASCII for lowercase     : 97-122
    ASCII for specials      : 33-47, 58-64, 91-96, 123-126
    ASCII for space         : 32 (considered special)

    converted to
    specials                : 32-47, 48-53, 54-59, 60-63
    integer                 : 64-73
    character               : 74-99 (selang-seling a dan A)
    '''
    orde = ord(char)

    integer     = (orde >= 48 and orde <= 57)
    uppercase   = (orde >= 65 and orde <= 90)
    lowercase   = (orde >= 97 and orde <= 122)
    specials1   = (orde >= 32 and orde <= 47)
    specials2   = (orde >= 59 and orde <= 64)
    specials3   = (orde >= 91 and orde <= 96)
    specials4   = (orde >= 123 and orde <= 126)

    if      specials1:  return orde
    elif    specials2:  return orde-11
    elif    specials3:  return orde-37
    elif    specials4:  return orde-63
    elif    integer:    return orde+16
    elif    uppercase:  return 75+2*(orde-65)
    elif    lowercase:  return 74+2*(orde-97)
    else: return 100

def search(data, query, file, option):
    # data : data yang dicari
    # query : jenis data ( dalam row apa )
    # file : nama file
    # option : pilihan ada dua, 'boolean' atau 'print',
    # jika memilih print maka akan menampilkan row yang dicari
    # contoh : search("babi", username, user_data, boolean)
    if option == 'boolean' :
        for row in file :
            if data == row[query] :
                return True
            else:
                return False
    elif option == 'print':
        for row in file :
            if data == row[query] :
                print(row)
    elif option == 'index':
        for i in range(panjang(file)):
            if data == file[i][query]:
                return i

def updateArrayElement(file, new_value, searchQuery, queryIndex, fileUpdateIndex):
    #file : nama array yang ingin diubah
    #new_value : nilai baru yang ingin diupdate
    #who : datanya
    #who index : data 'who' itu indeksnya keberapa
    #what_index : data 'what' itu indeks keberapa
    for i in file:
        if i[queryIndex] == searchQuery:
            i[fileUpdateIndex] = new_value
            return file

def updateArray(file, new_value, searchQuery, queryIndex):
    #file : nama array yang ingin diubah
    #new_value : nilai baru yang ingin diupdate
    #who : datanya
    #who index : data 'who' itu indeksnya keberapa
    #what_index : data 'what' itu indeks keberapa
    for i in file:
        if i[queryIndex] == searchQuery:
            i = new_value
            return file

def addToArray(array, entry):
    length = panjang(array)

    newArray = [0 for i in range(length+1)]
    for i in range(length+1):
        if i != length: 
            newArray[i] = array[i]
        else:
            newArray[i] = entry
    
    return newArray