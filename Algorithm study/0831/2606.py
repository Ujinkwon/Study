def bfs(v): 
    cnt = 0
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        cnt += 1
        for w in arr[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[w] + 1
    print(cnt-1)

com = int(input())
n = int(input())
arr = [[] for _ in range(com+1)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(com+1)
q = []
bfs(1)