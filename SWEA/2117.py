import sys
sys.stdin = open('2117.txt')

# 위치좌표 차이의 절대값 합 < 마름모 변의 길이 => 마름모 범위 내
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for a in range(n):
        for b in range(n):
            x, y = a, b
            for k in range(1,n+n):
                home = 0
                for i in range(n):
                    for j in range(n):
                        if abs(x-i) + abs(y-j) < k:
                            home += arr[i][j]
                price = home*m - (k*k + (k-1)*(k-1))
                if price >= 0 and cnt < home:
                    cnt = home

    print(f'#{tc} {cnt}')