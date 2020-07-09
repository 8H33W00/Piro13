h = int(input())
for i in range(h):
    for j in range(2 * h - 1):
        if (int((2 * h - 1) / 2)) - i <= j <= (int((2 * h - 1) / 2)) + i:
            print('*', end='')
        else:
            print(' ', end='')
    print()