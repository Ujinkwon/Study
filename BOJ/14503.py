import sys
from turtle import back
sys.stdin = open('14503.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
res = visited[r][c] = 1
    
while 1:
    flag = 0
    for _ in range(4):
        x = r + dx[(d+3) % 4]
        y = c + dy[(d+3) % 4]
        d = (d+3) % 4

        if 0 <= x < n and 0 <= y < m and not arr[x][y] and not visited[x][y]:
            visited[x][y] = 1
            res += 1
            c, r = y, x
            flag = 1
            break

    if not flag:
        if arr[r-dx[d]][c-dy[d]] == 1:
            print(res)
            break
        else:
            c, r = c-dy[d], r-dx[d]