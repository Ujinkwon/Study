c, r = map(int, input().split())
k = int(input())

board = [[0]*c for _ in range(r)]
board[0][0] = 1
move = [(1,0),(0,1),(-1,0),(0,-1)]
dir = 0
x,y = (0,0)
if k > c*r:
    print(0)
else:
    for i in range(2,k+1):
        while True:
            a,b = move[dir]
            a += x
            b += y
            if r > a >= 0 and c > b >= 0 and board[a][b] == 0:
                board[a][b] = i
                x, y = a, b
                break
            else:
                dir = (dir+1) % 4 
    print(y+1,x+1)