import modules

def foundgold(currentUser, gold):
    getgold = modules.randomchoice([2,4,6,8,10])
    if currentUser[8] >= 10 :
        getgold += getgold * 0.5
    gold = gold + getgold
    exp  = int(currentUser[9]) + 10
    currentUser[9] = str(exp)
    print("Lucky, you got "+ str(getgold)+" gold!")
    print("Experience + 10")
   
    return gold,currentUser
