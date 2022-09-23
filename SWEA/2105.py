import sys
sys.stdin = open('2105.txt')

def dfs(i, j, cafe, curr):
    global cnt
    if curr == (-1, 1) and i == y and j == x and cnt < len(cafe):
            cnt = len(cafe)
    else:
        for di, dj in pattern[curr]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and kind[ni][nj] not in cafe:
                visited[ni][nj] = 1
                cafe.append(kind[ni][nj])
                dfs(ni, nj, cafe, (di, dj))
                visited[ni][nj] = 0
                cafe.pop()

pattern = {
    (1,1) : [[1,1], [1,-1]],
    (1,-1) : [[1,-1], [-1,-1]],
    (-1,-1) : [[-1,-1], [-1,1]],
    (-1,1) : [[-1,1]],
}
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    kind = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    cnt = -1
    for y in range(n):
        for x in range(n):
            cafe = []
            dfs(y, x, cafe, (1,1))
    print(f'#{tc} {cnt}')