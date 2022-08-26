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
            if 0 <= x+dx[j] < n and 0 <= y+dy[j] < n and board[y+dy[j]][x+dx[j]] == 3-c:
                board[y+dy[j]][x+dx[j]] = c

        print(board)

    print(f'#{tc}')