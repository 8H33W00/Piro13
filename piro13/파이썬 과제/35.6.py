class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


    @classmethod #문자열로 인스턴스를 만드는 메소드로 클래스메소드 사용

    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':')) #:을 기준으로 분리한 뒤 int로 변환해서 각 변수에 넣어줌.
        return cls(hour, minute, second) #p에 hour,minute,second 값을 받음

    @staticmethod #문자열이 올바른 시간인지 검사하는 메소드로 클래스메소드 사용할 필요없음

    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':')) #:을 기준으로 분리한 뒤 int로 변환해서 각 변수에 넣어줌
        return 0 < hour<= 24 and 0 <= minute <= 59 and 0 <= second <= 60 #시간은 24시까지, 분은 59분까지,초는 60초까지 있어야함

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')
