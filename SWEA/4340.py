import sys
sys.stdin = open('4340.txt')

def dfs(i, j, type, cnt):
    global min_value
    if i == n-1 and j == n-1:
        if cnt < min_value:
            min_value = cnt
    elif cnt >= min_value:
        return
    else:
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        type = arr[i][j]
        if type == 1:
            d = [dir[0], dir[1]]
        elif type == 2:
            d = [dir[2], dir[3]]
        elif type == 3:
            d = [dir[0], dir[2]]
        elif type == 4:
            d = [dir[1], dir[2]]
        elif type == 5:
            d = [dir[1], dir[3]]
        elif type == 6:
            d = [dir[0], dir[3]]
        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= nj < n and 0 <= ni < n and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1)
                visited[ni][nj] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]   
    visited = [[0]*n for _ in range(n+1)]

    print(f'#{tc}')