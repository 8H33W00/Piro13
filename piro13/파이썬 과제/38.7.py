def palindrome(word):
    if list(word) == list(reversed(word)): #입력한 단어와 단어를 거꾸로 한 값이 같으면 입력값 출력
        print(word)
    else: #아니면 회문이 아니라는 문구 출력.
        print('회문이 아닙니다.')

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)