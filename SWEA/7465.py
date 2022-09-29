import sys
sys.stdin = open('7465.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    p = list(range(n+1))
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)
    res = set()
    for i in range(1, n+1):
        res.add(find_set(p[i]))
    print(f'#{tc} {len(res)}')