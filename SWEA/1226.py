import sys
sys.stdin = open('1226.txt')

def bfs(i, j, n):
    visited = [[0]*n for _ in range(n+1)]
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    si = sj = -1
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                si, sj = i, j
                break
        if si != -1:
            break

    print(f'#{tc} {bfs(si, sj, 16)}')