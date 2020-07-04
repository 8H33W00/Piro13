import random

class hero:
    def __init__(self, name, atk, dfs, hp):
        self.name = name
        self.atk = atk
        self.dfs = dfs
        self.hp = hp

    def attack(self, enemy):
        enemy.hp -= self.atk - enemy.dfs

    def character_info(self):
        print("이름:", self.name)
        print("공격력:", self.atk)
        print("방어력:", self.dfs)
        print("체력:", self.hp)

    def power_up(self, num):
        self.atk += num

IronMan = hero("IronMan", 70, 50, 100)
CaptainAmerica = hero("CaprtainAmerica", 60, 50, 100)
Thor = hero("Thor", 90, 20, 100)
Thanos = hero("Thanos", 100, 50, 300)

print("1. IronMan 2. CaptainAmerica 3. Thor")
num = int(input("당신의 캐릭터 번호를 선택해주세요(1, 2, 3):"))

selection = [IronMan, CaptainAmerica, Thor]
index_list = ['첫', '두', '세']

my_character = selection[num - 1]
selection.remove(my_character)
random.shuffle(selection)
selection.append(Thanos)

for key, value in enumerate(index_list):
    print(f'***{value} 번째 스테이지***')
    print('---내 캐릭터---')
    my_character.character_info()
    print('---적 캐릭터---')
    selection[key].character_info()
    print('--배틀--')
    print('')

    while True:
        my_character.attack(selection[key])
        if selection[key].hp <= 0:
            print('당신이 이겼습니다!')
            print('')
            my_character.hp = 100
            break
        selection[key].attack(my_character)
        if my_character.hp <= 0:
            print('당신이 졌습니다!')
            exit()

    if key == 0:
        my_character.dfs += 10
    if key == 1:
        my_character.atk += 10
        my_character.dfs += 10
        my_character.hp += 2001
