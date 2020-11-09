import modules

def foundgold(currentUser, gold):
    getgold = modules.randomchoice([2,4,6,8,10])
    gold = gold + getgold
    exp  = int(currentUser[9]) + 10
    currentUser[9] = str(exp)
    print("Lucky, you got "+ str(getgold)+" gold!")
    print("Experience + 10")

    return gold,currentUser
