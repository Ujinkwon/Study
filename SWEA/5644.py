import sys
sys.stdin = open('5644.txt')

def direction(n):
    if n == 1:
        dir = [-1, 0]
    elif n == 2:
        dir = [0, 1]
    elif n == 3:
        dir = [1, 0]
    elif n == 4:
        dir = [0, -1]
    else:
        dir = [0, 0]
    return dir

def move(arr, si, sj):
    flag = 0
    res = []
    res_p = []
    for k in arr:
        di, dj = direction(k)
        if not flag:
            ni, nj = si + di, sj + dj
            flag = 1
        else:
            ni += di
            nj += dj

        for q in range(a):
            if [ni, nj] in arr_bc[q]:
                if [ni, nj] not in res:
                    res.append([ni, nj])
                    res_p.append(arr_p[q])
                else:
                    if res_p[-1] < arr_p[q]:
                        res_p[-1] = arr_p[q]

    return res, res_p

t = int(input())
for tc in range(1, t+1):
    m, a = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_bc = [[] for _ in range(a)]
    arr_p = []
    for k in range(a):
        j, i, c, p = map(int, input().split())
        arr_p.append(p)
        for y in range(i-c, i+c+1):
            for x in range(j-c, j+c+1):
                if abs(y-i) + abs(x-j) <= c and 0 < y < 11 and 0 < x < 11:
                    arr_bc[k].append([y, x])

    a_move, a_p = move(arr_a, 1, 1)
    b_move, b_p = move(arr_b, 10, 10)

    cal = [0]*a

    sai = saj = 1
    sbi = sbj = 10
    flag_a = flag_b = 0
    for k in range(m):
        dai, daj = direction(arr_a[k])
        if not flag_a:
            nai, naj = sai + dai, saj + daj
            flag_a = 1
        else:
            nai += dai
            naj += daj

        dbi, dbj = direction(arr_b[k])
        if not flag_b:
            nbi, nbj = sbi + dbi, sbj + dbj
            flag_b = 1
        else:
            nbi += dbi
            nbj += dbj

        print(nai, naj, nbi, nbj)
        for q in range(a):
            if [nai, naj] in arr_bc[q]:
                print('a', arr_p[q], q)


            if [nbi, nbj] in arr_bc[q]:
                print('b', arr_p[q], q)
                if cal[q] != 0:
                    cal[q] = -(cal[q]+arr_p[q])








    print(f'#{tc}')