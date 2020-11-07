from random import choice
attack = 5 
magic = 5
luck = 1
defense = 0
health = 100
experience = 0
level = 100
gold = 0 
HealthSpider = 10
AttackSpider = 2
DamageSpider = 0
while True:
    ans = int(input("Do you want to explore ? \n1=Yes \n0=No \n")) # milih mau explore ato ngak
    print("\t\t---------------------------------------------------------------------------------")
    if ans == 0: # gak jadi explore
        print("We are heading home capt \n")
        break

    elif ans == 1: #jadi explore
        while True:
            explore = [1,2] #list sembarang buat nentuin kejadian (dapat treasure atau musuh)
            if choice(explore) == 1: # dapat monster
                print("You have met a tundra spider, will you fight or will you flee ( luck * 10% )? \nTundra spider stats: \nAttack: 2 \nDefense: 0 \nHealth: 10 \n")
                print("1. Run \n2. Fight") #pilihan kejadian
                choice_lari_ato_berantem = int(input("What would you do ? (1/2)\n")) #milih lari atau berantem
                choice1 = [1,2,3,4,5,6,7,8,9,10] #list sembarang buat nentuin kejadian (bisa lari atau tidak)               
                if choice(choice1) == 1 and choice_lari_ato_berantem == 1: #lari berhasil
                    luck += 1 #luck nambah
                    print("You successfully run from the tundra spider, that was a close one capt. You gain:",luck,"luck")
                    print("\t\t---------------------------------------------------------------------------------")
                    break

                else:
                    print("\nYou can't run, now face your fear!!!")
                    print("What action will you take? \n1. Strike - 2dmg \n2. Magic - 5dmg\n")
                    while HealthSpider != 0 or health != 0: # looping kalo darah player atau musuh != 0
                        choice_attack = int(input("Attack: (1/2)\n")) #milih tipe attack (strike or magic)
                        K = [1,2,3,4,5,6] #list sembarang lagi buat nentuin tipe kejadian pas ngelawan monster
                        if (((choice(K) == 1) or (choice(K) == 5)) and ((choice_attack  == 1) or (choice_attack == 2))): # serang
                            if choice_attack  == 1: # pake Strike
                                print("\nYou use strike")
                                HealthSpider -= attack #monster darahnya berkurang pake Strike attack
                                print("Success,Tundra spider took",attack,"dmg. Tundra spider health:",HealthSpider,"\n")
                                if HealthSpider == 0: #looping sampai monster darahnya = 0 
                                    break
                                
                            elif choice_attack  == 2: # pake Magic
                                print("\nYou use magic")
                                HealthSpider -= magic # monster darahnya ngurang pake Magic attack
                                print("Success,Tundra spider took",magic,"dmg. Tundra spider health:",HealthSpider,"\n")
                                if HealthSpider == 0: #looping sampai monster darahnya = 0 
                                    break
                        
                        elif ((choice(K) == 2) and ((choice_attack  == 1) or (choice_attack == 2))): #serangan meleset dan monster counter attack
                            print("\nYou missed, Spider health:", HealthSpider,"\n")

                        elif ((choice(K) == 3) and ((choice_attack  == 1) or (choice_attack == 2))): #serangan meleset dan monster counter attack
                            print("\nYou missed, Spider health:", HealthSpider,"And it counter attack")
                            attackCounter = 0.5*AttackSpider
                            health -= attackCounter
                            print("Your health is: ",health,"\n")
                            if health == 0: #player darahnya = 0
                                break
        
                        elif (((choice(K) == 4) or (choice(K) == 6)) and ((choice_attack  == 1) or (choice_attack == 2))): #gak bisa nyerang, karena monster yang nyerang
                            print("\nYou can't attack because it attacks you first") 
                            health -= AttackSpider
                            print("You take",AttackSpider,"damage, your health is:",health,"\n")
                            if health == 0: #player darahnya = 0
                                break

                    if health == 0: # health player 0, artinya player mati
                        print("\nYou died \n") 
                        break
                    
                    elif HealthSpider == 0: # health monster 0, artinya player menang
                        print("\nTundra spider is down. You win. \nYou get: \n+10 gold \n+50 Experience")
                        gold += 10
                        experience += 50
                        print("XP:",experience,"\nGold:",gold, "\n")
                        break
            
            elif choice(explore) == 2: # dapet random treasure
                gold+=10
                experience+=50
                print("\nLucky, you got 5 gold! \nExperience + 10")
                print("Your gold now is:",gold,"\nYour XP now is:",experience)
                print("\t\t---------------------------------------------------------------------------------\n")
                break         