
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}, 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1} 입니다. ".format(self.hp, self.damage))


marin1 = Unit("마린", 40, 5)
marin2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print(" ---- {0} ---- \n 유닛의 공격력은 {1} 입니다.".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True


if wraith2.clocking: # wraith2.clocking == True 이거랑 같은 뜻!
    print("---- {0} ---- \n 유닛은 현재 클로킹 상태 입니다. ".format(wraith2.name))




