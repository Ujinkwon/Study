import sys
sys.stdin = open('15486.txt')

for _ in range(4):
    n = int(input())
    time = pay = []
    for i in range(n):
        t, p = map(int, input().split())
        time.append(t)
        pay.append(p)

    print(time, pay)