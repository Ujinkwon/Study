import sys
sys.stdin = open('2667.txt')

def bfs(i, j, n):
    visited = [[0]*n for _ in range(n)]
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maparr[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        return visited

n = int(input())
maparr = [list(map(int, input())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maparr[i][j] == 1:
            si, sj = i, j
            break
print(si, sj)
print(bfs(si, sj, n))
