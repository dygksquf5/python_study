class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


# 이렇게 () 안에 상속 받을 부모클래스 정의해주고, 밑에 __init__ 함수 넣어주기! 그럼 부모클래스에 있는 값 그대로 상속받아 쓸 수 있음
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 시 방향으로 적군을 공격합니다. [공격력] : {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        self.hp -= damage
        print("{0}: {1} 만큼의 데미지를 받았습니다. \n ** 남은 체력 : {2} **".format(self.name, damage, self.hp))
        if self.hp <= 0:
            print("-------- \n{0} 파괴되었습니다. \n-------- ".format(self.name))


firebat1 = AttackUnit("파이어벳", 50, 10)
firebat1.attack(3)
firebat1.damaged(20)
