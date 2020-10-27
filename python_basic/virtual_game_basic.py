from random import *

# 기본 유닛 생성 클래스
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

        print("{0} : 생성되었습니다. 체력[{1}] ".format(self.name, self.hp))

    def move(self, location):
        print(" [ 지상유닛 이동합니다. ] ")
        print("{0} : {1}시 방향으로 이동합니다. 속도 [{2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        self.hp -= damage
        print("{0}: {1} 만큼의 데미지를 받았습니다. \n ** 남은 체력 : {2} **".format(self.name, damage, self.hp))
        if self.hp <= 0:
            print("-------- \n{0} 파괴되었습니다. \n-------- ".format(self.name))

    def attack(self, location):
        print("{0} : {1} 시 방향으로 적군을 공격합니다. [공격력] : {2}".format(self.name, location, self.damage))

class Bilding(Unit):
    def __init__(self, name, hp):
        Unit.__init__(self, name, hp, 0)


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


class Flyable:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, location):
        print("[ 공중유닛 이동 ]")


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, fly_speed)

    def move(self, location):
        print("[ 공중유닛이 이동합니다 ]")
        print(" {0}, {1} 시 방향으로 이동합니다. 속도 [{2}]".format(self.name, location, self.fly_speed))


class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. 체력이 10 줄어듭니다. 체력[{1}]".format(self.name, self.hp))
        else:
            print("{0} : 체력이 충분하지 않습니다. 사용이 불가능합니다. 체력[{1}]".format(self.name, self.hp))


class Tank(AttackUnit):
    seize_developted = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developted:
            return

        if not self.seize_mode:
            print("{0} : 시저모드로 변환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시저모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 30, 5)
        self.clocking = False

    def clock(self):
        if not self.clocking:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocking = True
        else:
            print("{0} : 클로킹 모드를 해합니다.".format(self.name))
            self.clocking = False


def start_game():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("[알림] 플레이어님이 게임을 퇴장하셨습니다.")


# while True:
#     game_state = input(" 게임을 시작하시겠습니까 ? o x ")
#     if game_state == "o":
#         start_game()
#         unit_state = input("어떤 종류의 유닛을 생성하시겠습니까? (숫자 입력) \n 1.마린 \n 2.탱크 \n 3.레이스 \n 입력 : ")
#         if unit_state == "1":
#             marin = Marin()
#         elif unit_state == "2":
#             tank = Tank()
#         elif unit_state == "3":
#             wraith = Wraith()
#         else:
#             print("잘못입력하셨습니다. 다시 입력 해 주세요.")
#     elif game_state == "x":
#         game_over()
#         break


start_game()

m1 = Marin()
m2 = Marin()
m3 = Marin()

t1 = Tank()
t2 = Tank()

wraith1 = Wraith()

attack_units = [m1, m2, m3]

attack_units.append(t1)
attack_units.append(t2)
attack_units.append(wraith1)


for units in attack_units:
    units.move(3)

Tank.seize_developted = True
print("[알림] 시저모드 개발이 완료되었습니다.")


for unit in attack_units:
    if isinstance(unit, Marin):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()

    elif isinstance(unit, Wraith):
        unit.clock()

for unit in attack_units:
    unit.attack("4")


for unit in attack_units:
    unit.damaged(randint(5, 21))


game_over()



