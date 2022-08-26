import sys
sys.stdin = open('4613.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    cnt = [[] for _ in range(n)]
    total = m-arr[0].count('W') + m-arr[n-1].count('R')
    color = 'W'

    for i in range(1, n-1):
        if color == 'W':
            if i != n-2:
                if arr[i].count('W') > arr[i].count('B'):
                    total += m - arr[i].count('W')
                    color = 'W'
                elif arr[i].count('W') <= arr[i].count('B'):
                    total += m - arr[i].count('B')
                    color = 'B'
            else:
                total += m - arr[i].count('B')
                color = 'B'

        elif color == 'B':
            if arr[i].count('B') > arr[i].count('R'):
                total += m - arr[i].count('B')
                color = 'B'
            elif arr[i].count('B') <= arr[i].count('R'):
                total += m - arr[i].count('R')
                color = 'R'

        print(color)
    print(f'#{tc} {total}')