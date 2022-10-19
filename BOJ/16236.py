import sys
sys.stdin = open('16236.txt')

def bfs(i, j):
    visited = [[0] * n for _ in range(n + 1)]
    q = [[i, j]]
    visited[i][j] = 1
    temp = []
    while q:
        i, j= q.pop(0)
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] <= shark and not visited[ni][nj]:
                visited[ni][nj] = visited[i][j] + 1
                q.append([ni, nj])
                if 0 < arr[ni][nj] < shark:
                    temp.append([ni, nj, visited[ni][nj]])
    return sorted(temp, key=lambda x: (x[2], x[0], x[1]))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
pos = []
cnt = res = eat = 0
shark = 2
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark_pos = [i, j]
            arr[i][j] = 0
while 1:
    temp = bfs(shark_pos[0], shark_pos[1])
    if not temp:
        break
    i, j, d = temp[0]
    arr[i][j] = 0
    eat += 1
    res += d-1
    shark_pos = [i, j]
    if eat == shark:
        eat = 0
        shark += 1
print(res)