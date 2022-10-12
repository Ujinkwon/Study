import sys
sys.stdin = open('4340.txt')

def dfs(i, j, type, cnt, dir):
    global min_value
    if i == n-1 and j == n-1:
        if cnt < min_value:
            min_value = cnt
    elif cnt >= min_value:
        return
    else:
        if 0 < type < 3:
            if dir == 'left':
                d = [[0, 1]]
            elif dir == 'right':
                d = [[0, -1]]
            elif dir == 'up':
                d = [[1, 0]]
            elif dir == 'down':
                d = [[-1, 0]]
        elif 2 < type < 7:
            if dir == 'left' or dir == 'right':
                d = [[1, 0], [-1, 0]]
            elif dir == 'up' or dir == 'down':
                d = [[0, 1], [0, -1]]

        for di, dj in d:
            ni, nj = i+di, j+dj
            if 0 <= nj < n and 0 <= ni < n and not visited[ni][nj] and arr[ni][nj] != 0:
                if di == 1:
                    dir = 'up'
                elif di == -1:
                    dir = 'down'
                elif dj == 1:
                    dir = 'left'
                elif dj == -1:
                    dir = 'right'
                visited[ni][nj] = 1
                dfs(ni, nj, arr[ni][nj], cnt+1, dir)
                visited[ni][nj] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]   
    visited = [[0]*n for _ in range(n+1)]
    min_value = 2500
    dfs(0, 0, arr[0][0], 1, 'left')
    print(f'#{tc} {min_value}')