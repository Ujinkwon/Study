import sys
sys.stdin = open('1258.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != -1:
                arr[i][j] = -1
                c_cnt = r_cnt = 1
                for a in range(1, n-i):
                    if arr[i+a][j] == 0:
                        break
                    elif arr[i+a][j] != -1:
                        arr[i+a][j] = -1
                        c_cnt += 1
                for b in range(1, n-j):
                    if arr[i][j+b] == 0:
                        break
                    elif arr[i][j+b] != -1:
                        arr[i][j+b] = -1
                        r_cnt += 1
                for v in range(i, i+c_cnt):
                    for w in range(j, j+r_cnt):
                        arr[v][w] = -1
                cnt.append([c_cnt, r_cnt])
                
    res = []
    for i in range(len(cnt)):
        res.append(cnt[i][0] * cnt[i][1])

    print(f'#{tc} {len(cnt)}', end=' ')

    min_value = 10000
    for l in range(len(cnt)):
        for i in range(len(res)):
            if res[i] <= min_value:
                if res[i] == min_value:
                    if cnt[i][0] < cnt[idx][0]:
                        min_value = res[i]
                        idx = i
                min_value = res[i]
                idx = i
        res[idx] = min_value = 10000
        print(*cnt[idx], end=' ')
    print()

