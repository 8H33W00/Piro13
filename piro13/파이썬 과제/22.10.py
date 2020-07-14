num1, num2 = map(int, input().split()) #입력 값 2개

if 1 <= num1 <= 20 and 10 <= num2 <= 30 and num1 < num2: #입력 값의 범위설정
    a =[2 ** i for i in range(num1, num2 + 1)] #조건문 2의 거듭제곱 = 2**i

a.pop(1), a.pop(-2) #리스트의 앞 뒤 2번째 요소 삭제
print(a)