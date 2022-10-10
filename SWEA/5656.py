import sys
from itertools import product
import copy
sys.stdin = open('5656.txt')

def runs(q, arr):
    while q:
        i, j = q.pop(0)
        for di, dj in [[i+arr[i][j]-1, j], [i-(arr[i][j]-1), j], [i, j+arr[i][j]-1], [i, j-(arr[i][j]-1)]]:
            arr[i][j] = 0
            if j == dj:
                    nj = j
                    if i < di:
                        s, e = i+1, di+1
                    else:
                        s, e = di, i
                    for ni in range(s, e):
                        if 0 <= ni < h:
                            if arr[ni][nj] > 1:
                                q.append([ni, nj])
                            else:
                                arr[ni][nj] = 0
            elif i == di:
                    ni = i
                    if j < dj:
                        s, e = j+1, dj+1
                    else:
                        s, e = dj, j
                    for nj in range(s, e):
                        if 0 <= nj < w:
                            if arr[ni][nj] > 1:
                                q.append([ni, nj])
                            else:
                                arr[ni][nj] = 0
        
    new_arr = [[]*w for _ in range(h)]
    for i in range(h):
        for j in range(w-1, -1, -1):
            if arr[j][i]:
                new_arr[i].append(arr[j][i])
    for i in new_arr:
        while len(i) != w:
            i.append(0)

    # 시계방향 90도 회전
    # new_arr = list(map(list, zip(*new_arr[::-1])))
    # 반시계방향 90도 회전
    arr = list(map(list, zip(*new_arr)))[::-1]
    return arr

t = int(input())
for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    cases = list(product(list(range(w)), repeat=n))
    res = []
    for case in cases:
        cnt = 0
        temp = copy.deepcopy(arr)
        for c in case:
            for i in range(h):
                if temp[i][c]:
                    q = [[i, c]]
                    temp = runs(q, temp)
                    break
                if not temp[h-1][c]:
                    break
        else:
            for p in range(h):
                for q in range(w):
                    if temp[p][q]:
                        cnt += 1
        res.append(cnt)
    print(min(res))