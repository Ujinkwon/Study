import sys
sys.stdin = open('4615.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    i = n // 2
    j = i - 1
    board[i][i] = board[j][j] = 2
    board[i][j] = board[j][i] = 1
    dx, dy = [0, 0, -1, 1, -1, 1, -1, 1], [-1, 1, 0, 0, -1, 1, 1, -1]

    for i in range(m):
        x, y, c = map(int, input().split())
        y, x = y-1, x-1
        board[y][x] = c
        for j in range(8):
            stack = []
            nx, ny = x, y
            while 1:
                nx += dx[j]
                ny += dy[j]
                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    stack.clear()
                    break
                elif board[ny][nx] == 0:
                    stack.clear()
                    break
                elif board[ny][nx] == c:
                    break
                else:
                    stack.append([nx,ny])
            for k in stack:
                board[k[1]][k[0]] = c
    res = [0,0]
    for i in range(n):
        res[0] += (board[i].count(1))
        res[1] += (board[i].count(2))

    print(f'#{tc}', *res)