import sys
sys.stdin = open('4340.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]   
    i, j = 0, 0
    flag, cnt = 1, 0
    while i != n-1 and j != n-1:
        if arr[i][j] == 1 or arr[i][j] == 2:
            if flag == 1:
                i, j = i, j+1
            elif flag == 2:
                i, j = i+1, j
            cnt += 1
        else:
            if flag == 1:
                if arr[i+1][j] != 0:
                    i, j = i+1, j
                else:
                    i, j = i-1, j
                flag = 2
            elif flag == 2:
                if arr[i][j+1] != 0:
                    i, j = i, j+1
                else:
                    i, j = i, j-1
                flag = 1
            cnt += 1
        print(i, j)
    print(cnt)
    print(f'#{tc}')