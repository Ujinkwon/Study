import sys
sys.stdin = open('1249.txt')

# def ff(i, j, total):
#     global min_value
#     if i == n-1 and j == n-1:
#         if total < min_value:
#             min_value = total
#     elif total >= min_value:
#         return
#     else:
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni, nj = i+di, j+dj
#             if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
#                 visited[ni][nj] = 1
#                 ff(ni, nj, total+arr[ni][nj])
#                 visited[ni][nj] = 0

# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     min_value = 9*n*n
#     ff(0,0,0)
#     print(f'#{tc} {min_value}')

def ff(i, j):
    visited[i][j] = 0
    q = [(i, j)]
    while q:
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n:
                plus = arr[ni][nj]
                if visited[ni][nj] > visited[i][j] + plus:
                    visited[ni][nj] = visited[i][j] + plus
                    q.append((ni, nj))

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[1000*200]*n for _ in range(n)]
    ff(0, 0)
    print(f'#{tc} {visited[n - 1][n - 1]}')