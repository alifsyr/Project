
def shop(currentUser, item_data, n):
    print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
    print("For sale:")
    if ((currentUser[10]) == "Windhelm"):
        num = 1
        dumm = [["ID", "Nama", "TipeItem", "Gold"]]
        for i in item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 1):
                    if (int(i[3]) == 0 & int(i[4] == 0)):
                        print(str(num), i[1], "+" + i[2], "atk", "(" + i[8], "gold)")
                        dumm = dumm + [[str(num), i[1], i[2]+"attack", i[8]]]
                    elif (int(i[2]) == 0 & int(i[4] == 0)):
                        print(str(num), i[1], "+" + i[3], "mgc", "(" + i[8], "gold)")
                        dumm = dumm + [[str(num), i[1], i[3]+"magic", i[8]]]
                    elif (int(i[2]) == 0 & int(i[3] == 0)):
                        print(str(num), i[1], "+" + i[4], "def", "(" + i[8], "gold)")
                        dumm = dumm + [[str(num), i[1], i[4]+"defense", i[8]]]
                    num += 1
        print("99.exit")

        print("You have", n, "gold")
        inp = int(input("buy: "))
        for i in dumm:
            if(i[0] != "ID"):
                if (inp == int(i[0])):
                    print("item", i[1], "has been bought add",i[2], "to player")
                    n = n-(int(i[3]))
                    print("your current gold is", n)
                elif (inp == int(i[0])):
                    print("item", i[1], "has been bought add",i[2], "to player")
                    n = n-(int(i[3]))
                    print("your current gold is", n)
                    n-(int(i[3]))
                elif (inp == int(i[0])):
                    print("item", i[1], "has been bought add",i[2], "to player")
                    n = n-(int(i[3]))
                    print("your current gold is", n)
                elif (inp == 99):
                    exit()

    elif ((currentUser[10]) == "Solitude"):
        num = 1
        dumm = [["ID", "Nama", "TipeItem", "Gold"]]
        for i in item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 2):
                    if (int(i[6]) == 0):
                        print(str(num), i[1], "+" + i[5],"luck", "("+i[8], "gold)")
                        dumm = dumm + [[str(num), i[1], i[5]+"luck", i[8]]]
                    elif (int(i[5]) == 0):
                        print(str(num), i[1], "+" + i[6],"HP", "("+i[8], "gold)")
                        dumm = dumm + [[str(num), i[1], i[6]+"HP", i[8]]]
                    num += 1
        print("99.exit")

        print("You have",  n, "gold")
        inp = int(input("buy: "))
        for i in dumm:
            if(i[0] != "ID"):
                if (inp == int(i[0])):
                    print("item", i[1], "has been bought add", i[2], "to player")
                    n = n-(int(i[3]))
                    print("your current gold is", n)
                elif (inp == int(i[0])):
                    print("item", i[1], "has been bought add", i[2], "to player")
                    n = n-(int(i[3]))
                    print("your current gold is", n)
                elif (inp == 99):
                    exit()
