import sys
sys.stdin = open('2573.txt')

def year():
    cntl = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt = 0
                for k in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    if 0 <= k[0] + i < n and 0 <= k[1] + j < m and arr[k[0]+i][k[1]+j] == 0:
                        cnt += 1
                cntl.append(cnt)
    k = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                arr[i][j] -= cntl[k]
                if arr[i][j] < 0:
                    arr[i][j] = 0
                k += 1
    return arr
 
def bfs(i, j, n, m):
    q = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt = 1
    return cnt

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cnt = res = 0
while cnt < 2:
    arr = year()
    visited = [[0]*m for _ in range(n)]
    cnt = no = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                cnt += bfs(i, j, n, m)
    res += 1
    for i in range(n):
        no += arr[i].count(0)
    if no == n*m:
        res = 0
        break
print(res)