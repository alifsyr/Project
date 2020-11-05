from main import dummy_array, final_boss
from F04_battleandexplore import battle

Alduskuy = final_boss(200, 60, 1000)


def alduskuy():
    print("You decided to fight the final boss")
    battle()

    Alduskuy_damage = Alduskuy.gen_dmg()
    print("Alduskuy Attack sebesar", Alduskuy_damage)

    Alduskuy_attacked = Alduskuy.dmg_taken()
    Alduskuy_HP = Alduskuy.hp_boss()
    print("Alduskuy took", Alduskuy_attacked,
          "and health dropped to", Alduskuy_HP)
