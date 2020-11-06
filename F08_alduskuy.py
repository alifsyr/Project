from object import final_boss
from F01_createdragonborn import createdragonborn
from F12_exitgame import exit

Alduskuy = final_boss(200, 60, 1000)


def alduskuy():
    print("You decided to fight the final boss")
    print("What action will you take?")
    print("1.Strike", "dmg")
    print("2.Magic")
    print("3.Flee")
    inp = int(input("Your choice here: "))

    Alduskuy_HP = Alduskuy.hp_boss()
    while ((Alduskuy_HP) != 0):
        if (inp == 1):
            # INI NANTI DIGANTI SAMA DARI CHARACTERNYA ADA DMG BRP SAMA ITEM APA
            Alduskuy_attacked = Alduskuy.dmg_taken(10)
            Alduskuy_HP = Alduskuy.hp_boss()
            print("Alduskuy took", Alduskuy_attacked,
                  "and health dropped to", Alduskuy_HP)
            if (Alduskuy_HP != 0):
                print("1.Strike", "dmg")
                print("2.Magic")
                print("3.Flee")
                inp = int(input("Your choice here: "))
            else:
                print("You have won the game!")
                print("You can create a new character or continue playing")
                choice = str(input())
                if (choice == "Create"):
                    createdragonborn()
                else:
                    exit()


alduskuy()
