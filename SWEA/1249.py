import sys
sys.stdin = open('1249.txt')

def ff(i, j, total):
    global min_value
    if i == n-1 and j == n-1:
        if total < min_value:
            min_value = total
    elif total >= min_value:
        return
    else:
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = 1
                ff(ni, nj, total+arr[ni][nj])
                visited[ni][nj] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    min_value = 9*n*n
    ff(0,0,0)
    print(f'#{tc} {min_value}')