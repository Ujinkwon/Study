import sys
sys.stdin = open('1215.txt')

for tc in range(1, 11):
    n = int(input())
    box = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8-n+1):
            arr = box[i][j:j+n]
            if arr == arr[::-1]:
                cnt += 1

    for i in range(8-n+1):
        for j in range(8):
            arr = ''
            for k in range(n):
                arr += box[i+k][j]
            if arr == arr[::-1]:
                cnt += 1
            
    print(f'#{tc} {cnt}')