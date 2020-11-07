
def shop(currentUser, item_data):
    print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
    print("For sale:")
    if ((currentUser[10]) == "Windhelm"):
        num = 1
        for i in item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 1):
                    if (int(i[3]) == 0 & int(i[4] == 0)):
                        print(str(num), i[1], "+" + i[2], "atk", "(" + i[8], "gold)")
                    elif (int(i[2]) == 0 & int(i[4] == 0)):
                        print(str(num), i[1], "+" + i[3], "mgc", "(" + i[8], "gold)")
                    elif (int(i[2]) == 0 & int(i[3] == 0)):
                        print(str(num), i[1], "+" + i[4], "def", "(" + i[8], "gold)")
                    num += 1
        print("You have 0 gold")
        print("buy: ")

    elif ((currentUser[10]) == "Solitude"):
        num = 1
        for i in item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 2):
                    if (int(i[6]) == 0):
                        print(str(num), i[1], "+" + i[5], "luck", "("+i[8], "gold)")
                    elif (int(i[5]) == 0):
                        print(str(num), i[1], "+" + i[6], "HP", "("+i[8], "gold)")
                    num += 1
        print("You have 0 gold")
        print("buy: ")