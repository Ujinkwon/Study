import sys
from itertools import combinations
sys.stdin = open('1251.txt')

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    case = list(combinations(list(range(n)), 2))
    q = []
    p = [i for i in range(n)]
    for u, v in case:
        d = (((x[u]-x[v])**2) + ((y[u]-y[v])**2))*e
        q.append([u, v, d])
    q.sort(key=lambda x:x[2])
    total, cnt = 0, 0
    while cnt < n-1:
        for u, v, d in q:
            if find_set(u) != find_set(v):
                union(u, v)
                total += d
                cnt += 1
    print(f'#{tc} {round(total)}')