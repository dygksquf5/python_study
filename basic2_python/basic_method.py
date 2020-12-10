class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}, 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1} 입니다. ".format(self.hp, self.damage))


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 시 방향으로 적군을 공격합니다. [공격력] : {2}".format(\
            self.name, location, self.damage))

    def damaged(self, damage):
        self.hp -= damage
        print("{0}: {1} 만큼의 데미지를 받았습니다. \n ** 남은 체력 : {2} **".format(self.name, damage, self.hp))
        if self.hp <= 0:
            print("-------- \n{0} 파괴되었습니다. \n-------- ".format(self.name))


firebat1 = AttackUnit("파이어벳", 50, 10)
firebat1.attack(3)
firebat1.damaged(10)
firebat1.damaged(10)
firebat1.damaged(10)
firebat1.damaged(10)
firebat1.damaged(10)