class Animal:
    def eat(self):
        print('먹다')


class Wing:
    def flap(self):
        print('파닥거리다')


class Bird(Animal,Wing): #Animal,Wing을 상속받은 Bird 클래스 생성
    def fly(self): #self로 모든 클래스의 메소드를 사용할 수 있음
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))