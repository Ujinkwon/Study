import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())

    while 1:
        if a > b:
            a //= 2
        elif a < b:
            b //= 2
        else:
            print(a*10)
            break