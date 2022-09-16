from itertools import count
import sys
sys.stdin = open('1953.txt')

def bfs(i, j, n, m):
    visited[i][j] = 1
    q = [(i, j)]
    check = [[1,2,5,6],[1,2,4,7],[1,3,4,5],[1,3,6,7]]
    while q:
        i, j = q.pop(0)
        type = under[i][j]
        if type == 1:
            d = [[0,1], [0,-1], [1,0], [-1,0]]
        elif type == 2:
            d = [[-1,0],[1,0]]
        elif type == 3:
            d = [[0,-1],[0,1]]
        elif type == 4:
            d = [[-1,0],[0,1]]
        elif type == 5:
            d = [[0,1],[1,0]]
        elif type == 6:
            d = [[1,0],[0,-1]]
        elif type == 7:
            d = [[-1,0],[0,-1]]
        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if (di == 0 and dj == 1 and under[ni][nj] in check[3]) or (di == 0 and dj == -1 and under[ni][nj] in check[2]) or (di == 1 and dj == 0 and under[ni][nj] in check[1]) or (di == -1 and dj == 0 and under[ni][nj] in check[0]):
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j]+1

        

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, t = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    bfs(r, c, n, m)
    res = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= t:
                res += 1
    print(f'#{tc} {res}')