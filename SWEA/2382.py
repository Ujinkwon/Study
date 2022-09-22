import sys
sys.stdin = open('2382.txt')

def move():
    for i in range(len(arr)):
        if arr[i][2] > 0:
            if arr[i][3] == 1:  # 상
                arr[i][0] -= 1
            elif arr[i][3] == 2:  # 하
                arr[i][0] += 1
            elif arr[i][3] == 3:  # 좌
                arr[i][1] -= 1
            elif arr[i][3] == 4:  # 우
                arr[i][1] += 1

            if arr[i][0] == 0 or arr[i][0] == n-1 or arr[i][1] == 0 or arr[i][1] == n-1:  # 약품이 칠해진 셀에 들어감
                arr[i][2] = arr[i][2]//2
                if arr[i][3] == 1:
                    arr[i][3] = 2
                elif arr[i][3] == 2:
                    arr[i][3] = 1
                elif arr[i][3] == 3:
                    arr[i][3] = 4
                elif arr[i][3] == 4:
                    arr[i][3] = 3

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]
    for _ in range(m):
        move()
        for i in range(len(arr)):
            maxvalue = arr[i][2]
            maxdir = arr[i][3]
            total = arr[i][2]
            for j in range(len(arr)):
                if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and i != j:
                    total += arr[j][2]
                    if maxvalue < arr[j][2]:
                        maxvalue = arr[j][2]
                        maxdir = arr[j][3]
                        arr[j][2] = 0
                        arr[j][3] = 0
                    else:
                        arr[j][2] = 0
                        arr[j][3] = 0
            arr[i][2] = total
            arr[i][3] = maxdir
    res = 0
    for i in arr:
        res += i[2]

    print(f'#{tc} {res}')