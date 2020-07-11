def check_group(word):
    last_alphabet = ""
    alphabets = []

    for letter in word:
        if letter == last_alphabet:
            continue
        else:
            if letter in alphabets:
                False

            alphabets.append(letter)
            last_alphabet = letter

    return True

count = int(input())
result = 0

for _ in range(count):
    word = input()

    if check_group(word):
        result += 1

print(result)