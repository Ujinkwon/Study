import sys

t = int(input())

for _ in range(t):
    n, char = sys.stdin.readline().split()
    for i in char:
        print(i * int(n), end='')
    print()