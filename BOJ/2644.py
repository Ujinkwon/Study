import sys
sys.stdin = open('2644.txt')

def bfs(s, g, v):
    visited = [0 for _ in range(v+1)]
    visited[s] = 1
    q = [s]
    while q:
        v = q.pop(0)
        if v == g:
            return visited[v] - 1
        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
print(bfs(a, b, n))