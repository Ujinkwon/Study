import sys
sys.stdin = open('2805.txt')

def oddsum(rs, re, ud):
    global total
    s = n // 2
    e = s+1
    for i in range(rs, re, ud):
        total += sum(farm[i][s:e])
        s -= 1
        e += 1
    return total

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    total = sum(farm[n//2])
    oddsum(0, n//2, 1)    # 위
    oddsum(n-1, n//2, -1)   # 아래
    print(f'#{tc} {total}')