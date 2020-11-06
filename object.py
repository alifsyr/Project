import random


class final_boss:
    def __init__(self, Attack, Defense, BOSS_HP):
        self.Attlow = -30
        self.Atthigh = +70
        self.MaxHP = BOSS_HP
        self.Def = Defense
        self.HP = BOSS_HP

    def gen_dmg(self):
        return random.randrange(self.Attlow, self.Atthigh)

    def hp_boss(self):
        return self.HP

    def dmg_taken(self, dmg):
        self.HP = self.HP - dmg
        if ((self.HP) <= 0):
            self.HP = 0
        return self.HP
