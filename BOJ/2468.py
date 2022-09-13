import sys
sys.stdin = open('2468.txt')
sys.setrecursionlimit(100000)  # 파이썬 인터프리터 stack에 최대 깊이 지정

def bfs(i, j, n, k):
    q = [(i, j)]
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] > k and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt = 1
    return cnt


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
min_value = 101
for i in range(n):
    if max(arr[i]) > max_value:
        max_value = max(arr[i])
    if min(arr[i]) < min_value:
        min_value = min(arr[i])
    
total = []
for k in range(min_value, max_value):
    visited = [[0]*n for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                res.append(bfs(i, j, n, k))
                total.append(sum(res))
if len(total) == 0:
    total = [1]
print(max(total))        