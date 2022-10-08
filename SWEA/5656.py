import sys
sys.stdin = open('5656.txt')

t = int(input())
for tc in range(1, t+1):
    n, w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]

    arr[1][2] = 0
    i, j = 2, 2
    q = []
    for di, dj in [[i+arr[i][j]-1, j], [i-(arr[i][j]-1), j], [i, j+arr[i][j]-1], [i, j-(arr[i][j]-1)]]:
        arr[i][j] = 0
        if 0 <= di < h and 0 <= dj < w:
            if j == dj:
                nj = j
                if i < di:
                    s, e = i+1, di+1
                else:
                    s, e = di, i
                for ni in range(s, e):
                    if arr[ni][nj] > 1:
                        q.append([ni, nj])
                    arr[ni][nj] = 0

            elif i == di:
                ni = i
                if j < dj:
                    s, e = j+1, dj+1
                else:
                    s, e = dj, j
                for nj in range(s, e):
                    if arr[ni][nj] > 1:
                        q.append([ni, nj])
                    arr[ni][nj] = 0
    for i in arr:
        print(i)
    print(q)