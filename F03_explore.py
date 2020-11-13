import modules

def explore(currentUser):
    result = modules.randomrange(500)
    if result >= (500 - int(currentUser[8])):
        gold = True
        return  gold
    else:
        gold = False
        return gold