import sys
sys.stdin = open('1926.txt')

def bfs(i, j, n, m):
    global draw
    visited = [[0]*m for _ in range(n)]
    q = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and draw[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                cnt += 1
    for i in range(n):
        for j in range(m):
            if visited[i][j] != 0:
                draw[i][j] = 0
    return cnt

n, m = map(int, input().split())
draw = [list(map(int, input().split())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1:
            res.append(bfs(i, j, n, m))

print(len(res))
if len(res) == 0:
    print(0)
else:
    print(max(res))
