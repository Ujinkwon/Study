t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    for j in range(min(a, b), 0, -1):
        if a % j == 0 and b % j == 0:
            ret = j
            break
    print(int(a*b/j))