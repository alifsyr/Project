def attribute(currentUser, gold):
    print("Attack : "+currentUser[5])
    print("Magic : "+currentUser[6])
    print("Defense : "+currentUser[7])
    print("Luck : "+currentUser[8])
    print("Gold : "+str(gold))
    print("Experience : "+currentUser[9])
    print("Level : "+currentUser[4])
    if currentUser[10] == '1':
        print("City : Windhelm")
    else:
        print("City : Solitude")
