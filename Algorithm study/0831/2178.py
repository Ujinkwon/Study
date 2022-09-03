def bfs(i, j, n, m):
    visited = [[0]*m for _ in range(n)]
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if miro[i][j] == 3:
            return visited[i][j]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and miro[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]
miro[n-1][m-1] = 3
print(bfs(0,0,n, m))