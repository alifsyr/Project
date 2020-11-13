def shop(currentUser, item_data):
    exit = False
    while (not exit):
        print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
        print("For sale:")
        item = []
        item = listdata(item_data,currentUser,item)
        print("{:<8} {:<30} {:<8} {:<8} {:<8}".format('No','Item Name','Value','Type','Price'))
        for i in item:
            No,Item,Value,Type,Price = i
            print("{:<8} {:<30} {:<8} {:<8} {:<8}".format(No,Item,"+"+Value,Type,Price))
        print("99.exit")
        exit, currentUser = buy(item, currentUser, exit)

    return currentUser

def buy(item, currentUser, exit):
    print("You have", currentUser[12], "gold")
    inp = int(input("buy: "))
    for i in item:
        if(i[0] != "ID"):
            if (inp == int(i[0])):
                gold = int(currentUser[12]) - int(i[4])
                currentUser[12] = str(gold)

                if gold <= 0 :
                    gold = int(currentUser[12]) + int(i[4])
                    currentUser[12] = str(gold)
                    print("You gold are not enough")

                elif gold > 0:
                    print("item", i[1], "has been bought add",i[2], i[3],"to player")
                    currentUser = upgrade(item,currentUser,inp)
                    print("your current gold is", currentUser[12])

            elif (inp == 99):
                exit = True

    return exit, currentUser

def listdata(item_data, currentUser,item):
    num = 1
    for i in item_data:
        if(i[0] != "ID"):
            if(i[7] == currentUser[10]):
                if (int(i[3]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    item = item + [[str(num), i[1], i[2], "attack", i[8]]]

                elif (int(i[2]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    item = item + [[str(num), i[1], i[3], "magic", i[8]]]

                elif (int(i[3]) == 0 and int(i[2]) == 0 and int(i[5]) == 0 and int(i[6]) == 0):
                    item = item + [[str(num), i[1], i[4], "defense", i[8]]]

                elif (int(i[3]) == 0 and int(i[4]) == 0 and int(i[2]) == 0 and int(i[6]) == 0):
                    item = item + [[str(num), i[1], i[5], "luck", i[8]]]

                elif (int(i[3]) == 0 and int(i[4]) == 0 and int(i[5]) == 0 and int(i[2]) == 0):
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
