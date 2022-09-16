import sys
sys.stdin = open('1238.txt')

def bfs(s):
    visited[s] = 1
    q = [s]
    while q:
        v = q.pop(0)
        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v]+1

for tc in range(1, 11):
    l, s = map(int, input().split())
    data = list(map(int, input().split()))
    arr = [[] for _ in range(max(data)+1)]
    visited = [0 for _ in range(max(data)+1)]
    for i in range(0, l, 2):
        if data[i+1] not in arr[data[i]]:
            arr[data[i]].append(data[i+1])
    bfs(s)
    z = max(visited)
    for i in range(max(data), -1, -1):
        if visited[i] == z:
            res = i
            break
    print(f'#{tc} {res}')