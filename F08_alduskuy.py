from object import final_boss
from F04_battleandexplore import battle
from F01_createdragonborn import createdragonborn
from F03_explore import explore

Alduskuy = final_boss(200, 60, 1000)


def alduskuy():
    print("You decided to fight the final boss")
    battle()

    Alduskuy_damage = Alduskuy.gen_dmg()
    print("Alduskuy Attack sebesar", Alduskuy_damage)

    Alduskuy_attacked = Alduskuy.dmg_taken()
    Alduskuy_HP = Alduskuy.hp_boss()
    print("Alduskuy took", Alduskuy_attacked,"and health dropped to", Alduskuy_HP)
    Alduskuy_Death = Alduskuy.boss_death()
    if (Alduskuy_Death):
        print("You have won the game!")
        print("You can create a new character or continue playing")
        choice = str(input())
        if (choice == "Create"):
            createdragonborn()
        else:
            explore()
