import sys
sys.stdin = open('17144.txt')


def diffusion(i, j, temp):
    n = arr[i][j] // 5
    total = 0
    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        ni, nj = i+di, j+dj
        if 0 <= ni < r and 0 <= nj < c and not((ni == wind and nj == 0) or (ni == wind+1 and nj == 0)):
            temp[ni][nj] += n
            total += n
    temp[i][j] += (arr[i][j] - total)
    return temp

def move(temp):
    # 위 => 아래
    for i in range(wind - 1, 0, -1):
        temp[i][0] = temp[i - 1][0]
    # 오 => 왼
    for j in range(7):
        temp[0][j] = temp[0][j + 1]
    # 아래 => 위
    for i in range(wind):
        temp[i][7] = temp[i + 1][7]
    # 왼 => 오
    for j in range(7, 0, -1):
        temp[wind][j] = temp[wind][j - 1]

    # 아래 => 위
    for i in range(wind + 2, 6):
        temp[i][0] = temp[i + 1][0]
    # 오 => 왼
    for j in range(7):
        temp[6][j] = temp[6][j + 1]
    # 위 => 아래
    for i in range(6, wind + 1, -1):
        temp[i][7] = temp[i - 1][7]
    # 왼 => 오
    for j in range(7, 0, -1):
        temp[wind + 1][j] = temp[wind + 1][j - 1]
    return temp

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if arr[i][0] == -1:
        wind = i
        break
for _ in range(t):
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                temp = diffusion(i, j, temp)
    arr = move(temp)

res = 0
for i in arr:
    res += sum(i)
print(res)
