import sys, copy
sys.stdin = open('1221.txt')

def lad(x, ladder):
    global cnt, res
    cnt, y = 0, 98
    while y > 0:
        if x > 0 and ladder[y][x-1] == 1:
            ladder[y][x] = 0
            x -= 1
        if x < 99 and ladder[y][x+1] == 1:
            ladder[y][x] = 0
            x += 1
        elif ladder[y-1][x] == 1:
            y -= 1
        cnt += 1
    cntarr.append(cnt)
    res.append(x)

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    end, res, cntarr = [], [], []
    for i in range(100):
        if ladder[99][i] == 1:
            end.append(i)
    for i in end:
        nladder = copy.deepcopy(ladder)
        lad(i, nladder)
    print(f'#{tc} {res[cntarr.index(min(cntarr))]}')