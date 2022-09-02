import sys
sys.stdin = open('2667.txt')

def bfs(i, j, n):
    global home
    visited = [[0]*n for _ in range(n)]
    q = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and home[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                cnt += 1
                visited[ni][nj] = visited[i][j] + 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] != 0:
                home[i][j] = 0
    return cnt

n = int(input())
home = [list(map(int, input())) for _ in range(n)]
cntarr = []
si = sj = -1
for i in range(n):
    for j in range(n):
        if home[i][j] == 1:
            cntarr.append(bfs(i, j, n))
res = sorted(cntarr)
print(len(res))
for i in res:
    print(i)