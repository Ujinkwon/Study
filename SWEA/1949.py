import sys
import copy
sys.stdin = open('1949.txt')

def dfs(i, j, cnt, arr):
    global max_cnt
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            if arr[i][j] > arr[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1, arr)
                visited[ni][nj] = 0
            else:
                if cnt >= max_cnt:
                    max_cnt = cnt
    return max_cnt

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n+1)]

    # 최댓값 위치 찾기
    max_value = 0
    q = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > max_value:
                max_value = arr[i][j]
                q = [[i, j]]
            elif arr[i][j] == max_value:
                q.append([i, j])
    # 지형의 가능한 케이스
    case = [arr]
    for i in range(n):
        for j in range(n):
            temp = copy.deepcopy(arr)
            for p in range(1, k+1):
                temp2 = copy.deepcopy(temp)
                temp2[i][j] -= p
                case.append(temp2)
    # 각 위치에서 최대 경로 찾기
    res = []
    while q:
        i, j = q.pop()
        for c in case:
            max_cnt = 0
            visited[i][j] = 1
            res.append(dfs(i, j, 1, c))
            visited[i][j] = 0
    print(f'#{tc} {max(res)}')