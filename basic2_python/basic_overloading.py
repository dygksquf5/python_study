class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛 이동합니다.]")
        print("{0}, {1} 시 방향으로 이동합니다. 속도 [{1}]".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 시 방향으로 적군을 공격합니다. [공격력] : {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        self.hp -= damage
        print("{0}: {1} 만큼의 데미지를 받았습니다. \n ** 남은 체력 : {2} **".format(self.name, damage, self.hp))
        if self.hp <= 0:
            print("-------- \n{0} 파괴되었습니다. \n-------- ".format(self.name))


# 날 수 있고 공격도 가능한 유닛 만들기

class Flyable:
    def __init__(self, fly_Speed):
        self.fly_Speed = fly_Speed

    def fly(self, name, location):
        print("{0} : {1}시 방향으로 날아갑니다. 속도 [{2}]".format(name, location, self.fly_Speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_Speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, fly_Speed)

    def move(self, location):
        print("[공중유닛이 이동합니다.]")
        print(" {0}, {1} 시 방향으로 이동합니다. 속도 [{2}]".format(self.name, location, self.fly_Speed))


marin1 = AttackUnit("마린", 20, 10, 5)
marin1.move(5)

battle_ship1 = FlyableAttackUnit("배틀쉽", 300, 30, 3)
battle_ship1.move(3)