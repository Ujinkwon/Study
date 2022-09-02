import sys
sys.stdin = open('7576.txt')

def bfs(i, j, m, n):
    global tomato
    visited = [[0]*m for _ in range(n)]
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and tomato[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                tomato[i][j] = 1
    return 1

for _ in range(5):
    m, n  = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                print(bfs(i, j, m, n))
