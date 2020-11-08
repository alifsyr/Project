
def shop(currentUser, item_data, n):
    print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
    print("For sale:")
    item = [["ID", "Nama", "Besar", "Tipe", "Gold"]]
    item = printitem(item_data,currentUser,item)
    print("99.exit")
    buy(n, item)

def buy(n,item):
    print("You have", n, "gold")
    inp = int(input("buy: "))
    for i in item:
        if(i[0] != "ID"):
            if (inp == int(i[0])):
                print("item", i[1], "has been bought add",i[2], i[3],"to player")
                n = n-(int(i[4]))
                print("your current gold is", n)
            elif (inp == 99):
                exit()

def printitem(item_data, currentUser,item):
    num = 1
    for i in item_data:
        if(i[0] != "ID"):
            if(i[7] == currentUser[10]):
                if (int(i[3]) == 0 & int(i[4]) == 0 & int(i[5]) == 0 & int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[2], "atk", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[2], "attack", i[8]]]

                elif (int(i[2]) == 0 & int(i[4]) == 0 & int(i[5]) == 0 & int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[3], "mgc", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[3], "magic", i[8]]]

                elif (int(i[3]) == 0 & int(i[2]) == 0 & int(i[5]) == 0 & int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[4], "def", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[4], "defense", i[8]]]

                elif (int(i[3]) == 0 & int(i[4]) == 0 & int(i[2]) == 0 & int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[5], "luck", "("+i[8], "gold)")
                    item = item + [[str(num), i[1], i[5], "luck", i[8]]]

                elif (int(i[3]) == 0 & int(i[4]) == 0 & int(i[5]) == 0 & int(i[2]) == 0):
                    print(str(num), i[1], "+" + i[6], "HP", "("+i[8], "gold)")
                    item = item + [[str(num), i[1], i[6], "HP", i[8]]]

                num += 1

    return item