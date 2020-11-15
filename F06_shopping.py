
def shop(currentUser, item_data, n):
    exit = False
    gold = n 
    while (not exit):
        print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
        print("For sale:")
        item = [["ID", "Nama", "Besar", "Tipe", "Gold"]]
        item = printitem(item_data,currentUser,item)
        print("99.exit")
        gold, exit, currentUser = buy(gold, item, currentUser, exit)

    return gold, currentUser

def buy(gold, item, currentUser, exit):
    print("You have", gold, "gold")
    inp = int(input("buy: "))
    for i in item:
        if(i[0] != "ID"):
            if (inp == int(i[0])):
                gold = gold - (int(i[4]))

                if gold <= 0 :
                    gold = gold + int(i[4])
                    print("You gold are not enough")

                elif gold > 0:
                    print("item", i[1], "has been bought add",i[2], i[3],"to player")
                    currentUser = upgrade(item,currentUser,inp)
                    print("your current gold is", gold)

            elif (inp == 99):
                exit = True

    return gold, exit, currentUser

def printitem(item_data, currentUser,item):
    num = 1
    for i in item_data:
        if(i[0] != "ID"):
            if(i[7] == currentUser[10]):
                if (int(i[3]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[2], "atk", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[2], "attack", i[8]]]

                elif (int(i[2]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[3], "mgc", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[3], "magic", i[8]]]

                elif (int(i[3]) == 0 and int(i[2]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[4], "def", "(" + i[8], "gold)")
                    item = item + [[str(num), i[1], i[4], "defense", i[8]]]

                elif (int(i[3]) == 0 and int(i[4]) == 0 and int(i[2]) == 0 and int(i[6]) == 0):
                    print(str(num), i[1], "+" + i[5], "luck", "("+i[8], "gold)")
                    item = item + [[str(num), i[1], i[5], "luck", i[8]]]

                elif (int(i[3]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[2]) == 0):
                    print(str(num), i[1], "+" + i[6], "HP", "("+i[8], "gold)")
                    item = item + [[str(num), i[1], i[6], "HP", i[8]]]

                num += 1

    return item

def upgrade(item,currentUser,inp):
    for i in item:
        if i[0] != 'ID':
            if inp == int(i[0]):
                if i[3] == 'attack':
                    upgrade = int(currentUser[5]) + int(i[2])
                    currentUser[5] = str(upgrade)

                    return currentUser

                elif i[3] == 'magic':
                    upgrade = int(currentUser[6]) + int(i[2])
                    currentUser[6] = str(upgrade)

                    return currentUser

                elif i[3] == 'luck':
                    upgrade = int(currentUser[8]) + int(i[2])
                    currentUser[8] = str(upgrade)

                    return currentUser
                
                elif i[3] == 'HP':
                    upgrade = int(currentUser[3]) + int(i[2])
                    if upgrade >= int(currentUser[2]):
                        currentUser[3] = currentUser[2]
                        print("Your HP is already maximum")

                        return currentUser
                    
                    else:
                        currentUser[3] = str(upgrade)

                        return currentUser

                elif i[3] == 'defense':
                    upgrade = int(currentUser[7]) + int(i[2])
                    currentUser[7] = str(upgrade)


                    return currentUser
