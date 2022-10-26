import sys
sys.stdin = open('14510.txt')

t = int(input())
for tc in range(1, t+1):
    odd = even = 0
    n = int(input())
    tree = list(map(int, input().split()))
    best = max(tree)
    for i in range(n):
        odd += (best - tree[i]) % 2
        even += (best - tree[i]) // 2
    temp = max(even-odd, 0)
    odd2 = temp*2
    even -= temp
    day = 0
    if even:
        day = even*2
        if odd < even:
            odd2 -= (even-odd)
            odd = 0
        else:
            odd -= even
    while odd2 > 0:
        day += 1
        if day % 2:
            odd2 -= 1
        else:
            odd2 -= 2
    print(day)
    if odd > 0 and day:
        day += 1
        if not day % 2:
            day += 1
    print(day, odd)
    while odd > 0:
        day += 2
        odd -= 1
    print(f'#{tc} {day}')