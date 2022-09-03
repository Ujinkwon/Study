def dfs(v):
    visited[v] = 1
    result.append(v)
    for w in arr[v]:
        if visited[w] == 0:
            dfs(w)

def bfs(v): 
    q.append(v)
    visited2[v] = 1
    while q:
        v = q.pop(0)
        print(v, end=' ')
        for w in arr[v]:
            if not visited2[w]:
                q.append(w)
                visited2[w] = visited2[w] + 1

n, m, s = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a] = sorted(arr[a])
    arr[b] = sorted(arr[b])

visited = [0]*(n+1)
result, q = [], []
dfs(s)
print(*result)
visited2 = [0] * (n+1)
bfs(s)