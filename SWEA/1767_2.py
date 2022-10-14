import sys
sys.stdin = open('1767.txt')

def ff(idx, total, core):
    global min_value
    global max_core
    if idx == len(q):
        if core > max_core:
            max_core = core
            min_value = total
        elif core == max_core:
            if total < min_value:
                min_value = total

    else:
        i, j = q[idx]
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            cnt = 0
            dir = []
            flag = 1
            while 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and not arr[ni][nj]:
                    dir.append([ni, nj])
                    cnt += 1
                    ni += di
                    nj += dj
                else:
                    dir = []
                    cnt = 0
                    flag = 0
                    break
            for a in dir:
                visited[a[0]][a[1]] = 1
            ff(idx+1, total+cnt, core+flag)
            for a in dir:
                visited[a[0]][a[1]] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j]:
                q.append([i, j])
    min_value = 144
    max_core = 0
    ff(0, 0, 0)

    print(f'#{tc} {min_value}')