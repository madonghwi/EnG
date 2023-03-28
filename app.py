import random
import numpy

class Player:
    def __init__(self, name, hp, power, axe):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.normal_attack = "공격"
        self.throwing = "던지기"
        self.throwing_axe = axe
        self.throwing_axe_power = 17

    def attack(self, attack_type):
        if attack_type == self.normal_attack:
            attack_power = random.randint(int(self.power * 0.9), int(self.power * 1.2))
        elif attack_type == self.throwing:
            if self.throwing_axe < 1:
                print("남은 도끼가 없다")
                return False
            self.throwing_axe -= 1
            attack_power = self.throwing_axe_power
        else:
            print("그렇게 할 수 없다")
            return False

        return attack_power


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.normal_attack = "공격"

    def attack(self):
        damage = random.randint(int(self.power * 0.7), int(self.power * 1.3))
        return damage


def print_status(player, monster):
    print(f"{player.name}:HP {player.hp}/{player.max_hp}, 투척용 도끼 {player.throwing_axe}자루")
    print(f"{monster.name}:HP {monster.hp}/{monster.max_hp}")


# 모험의 시작
player_name = input("플레이어의 이름을 입력")
player = Player(player_name, hp=150, power=10, axe=5)

# 몬스터
monsters = [
    Monster("고블린", hp=50, power=6),
    Monster("늑대", hp=70, power=7),
    Monster("오크", hp=150, power=10),
    Monster("와이번", hp=512, power=30)
]
monster = numpy.random.choice(monsters, p=[0.4, 0.3, 0.2, 0.1])



print(f"[{monster.name} 조우]")

# 전투
while player.hp > 0 and monster.hp > 0:
    print_status(player, monster)

    # 플레이어 공격
    while True:
        attack_type = input("(공격, 던지기)을/를 한다")
        attack_power = player.attack(attack_type)
        monster.hp -= attack_power
        print(f"{player.name}의 {attack_type} {monster.name}에게 {attack_power}의 데미지")
        if attack_power:
            break

    if monster.hp <= 0:
        print(f"[{monster.name}] 격파")
        break

    # 몬스터 공격
    attack_power_m = monster.attack()
    player.hp -= monster.attack()
    print(f"{monster.name}의 {monster.normal_attack} {player.name}에게 {attack_power_m}의 데미지")

    if player.hp <= 0:
        print(f"YOU DIED")
        break