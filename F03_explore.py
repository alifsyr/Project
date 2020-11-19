import modules

def explore(currentUser):
    # fungsi yang berguna merandom kejadian
    result = modules.randomrange(501) # randomize kejadian menggunakan integer dengan range 0-500
    if result >= (500 - int(currentUser[8])): # apabila angka yang di random >= angak 500 - luck maka akan mendapat gold
        gold = True
        return  gold
    else: # apabila tidak akan bertemu monster
        gold = False
        return gold