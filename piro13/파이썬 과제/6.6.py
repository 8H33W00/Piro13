#a, b, c = map(int, input().split())
#print(a + b + c)

#a = 50
#b = 100
#c = None

#print(a)
#print(b)
#print(c)

#a , b, c, d = map(int, input().split())
#print(int((a + b + c + d) / 4))

#print(16, 9, sep=':')

#ear, month, day, hour, minute, second = input().split()

#print(year, month,day, sep='-', end='T')
#print(hour, minute, second, sep=':')

#a, b, c, d = map(int, input().split())
#print(a >= 90 and b > 80 and c > 85 and d >= 80)

#a = int(input())
#print(tuple(range(-10, 10, a)))

#a = input().split()
#b = map(float, input().split())
#c = dict(zip(a, b))
#print(c)

age = int(input())
balance = 9000

if age < 7:
    print("7세 이상 이용")
elif 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
else:
    balance -= 1250
print(balance)