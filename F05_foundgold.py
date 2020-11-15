import modules

def foundgold(currentUser):
    getgold = modules.randomchoice([2,4,6,8,10])
    gold = int(currentUser[12]) + getgold
    exp  = int(currentUser[9]) + 10
    currentUser[12] = str(gold)
    currentUser[9] = str(exp)
    print("Lucky, you got "+ str(getgold)+" gold!")
    print("Experience + 10")

    return currentUser
