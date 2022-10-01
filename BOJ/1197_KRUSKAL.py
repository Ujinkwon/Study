import sys
sys.stdin = open('1197.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

v, e = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(e)]
arr.sort(key=lambda x:x[2])
p = [i for i in range(v+1)]

cnt, total = 0, 0
for n1, n2, w in arr:
    if find_set(n1) != find_set(n2):
        cnt += 1
        total += w
        union(n1, n2)
        if cnt == v:
            break
print(total)