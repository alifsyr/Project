import modules

def foundgold(currentUser):
    getgold = modules.randomchoice([2,4,6,8,10])
    getexp = modules.randomchoice([10,20,30,40,10])
    if currentUser[8] >= 10 :
        getgold += getgold * 0.5
    currentUser[12] +=  getgold
    currentUser[9] += getexp 
    print("Lucky, you got "+ str(getgold)+" gold!")
    print("Experience + 10")
   
    return currentUser
