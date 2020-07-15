class Annie:  # Annie 클래스 생성

    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana  # 모든 매개변수를 속성으로 만들어줌
        self.ability_power = ability_power

    def tibbers(self):  # Annie 클래스에 tibbers 메소드를 만들고 피해량 출력
        print('티버: 피해량 {0}'.format(self.ability_power * 0.65 + 400))


health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()