
def shopping(Item_data, currentUser):
    print("Everything's for sale my friend. Everything. If I had a sister, I'd sell her in a second")
    print("For sale:")
    if ((currentUser[11]) == "Windhelm"):
        num = 1
        for i in Item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 1):
                    if (int(i[3])==0 & int(i[4]==0)):
                        print((str(num), str(i[1]), "+", str(i[2]),"atk", "(", str(i[8])), "gold)")
                    elif (int(i[2])==0 & int(i[4]==0)):
                        print((str(num), str(i[1]), "+", str(i[3]),"mgc", "(", str(i[8])), "gold)")
                    elif (int(i[2])==0 & int(i[3]==0)):
                        print((str(num), str(i[1]), "+", str(i[4]),"def", "(", str(i[8])), "gold)")
                    num +=1
    elif ((currentUser[11]) == "Solitude"):
        num = 1
        for i in Item_data:
            if(i[0] != "ID"):
                if(int(i[7]) == 2):
                    if (int(i[6])==0):
                        print((str(num), str(i[1]), "+", str(i[5]),"luck", "(", str(i[8])), "gold)")
                    elif (int(i[5])==0 ):
                        print((str(num), str(i[1]), "+", str(i[6]),"HP", "(", str(i[8])), "gold)")
                    num +=1


