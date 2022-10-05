def find_set(x):
    if x != p[x]:
        return find_set(p[x])
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n)]
adj = []
for i in range(n):
    for j in range(i+1, n):
        adj.append((arr[i][j], i, j))
adj.sort()
res = 0
for k in adj:
    w, i, j = k
    if find_set(i) != find_set(j):
        union(i, j)
        res += w
print(res)