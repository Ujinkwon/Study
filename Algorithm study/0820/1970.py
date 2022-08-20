import sys
sys.stdin = open('1970.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    print(f'#{tc}')
    for i in range(8):
        print(n // money[i], end=' ')
        n = n % money[i]
    print()
