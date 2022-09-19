import sys
sys.stdin = open('1240.txt')

pattern = [
    [0,0,0,1,1,0,1],
    [0,0,1,1,0,0,1],
    [0,0,1,0,0,1,1],
    [0,1,1,1,1,0,1],
    [0,1,0,0,0,1,1],
    [0,1,1,0,0,0,1],
    [0,1,0,1,1,1,1],
    [0,1,1,1,0,1,1],
    [0,1,1,0,1,1,1],
    [0,0,0,1,0,1,1]
]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 1:
                y, x = i, j
                break
    arr = arr[y][(x-55):x+1]
    odd = even = 0
    c = 0
    while arr:
        c += 1
        if c % 2:
            odd += pattern.index(arr[:7])
        else:
            even += pattern.index(arr[:7])
        arr = arr[7:]

    ans = 0
    if (odd*3 + even) % 10 == 0:
        ans = odd+even
    print(f'#{tc} {ans}')