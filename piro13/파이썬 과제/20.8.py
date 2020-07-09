a, b = map(int, input().split())
for i in range(a, b + 1):
    if 1 <= a <= 1000 and 10 <= b <= 1000:
        if i % 5 == 0 and i % 7==0:
            print('FizzBuzz')
        elif i % 5==0:
            print('Fizz')
        elif i % 7==0:
            print('Buzz')
        else:
            print(i)