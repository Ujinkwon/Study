import sys
sys.stdin = open('4613.txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    min_value = n * m

    cnt1 = 0
    for i in range(n-2):
        cnt1 += (m - arr[i].count('W'))
        cnt2 = 0
        for a in range(i+1, n-1):
            cnt2 += (m - arr[a].count('B'))
            cnt3 = 0
            for p in range(a+1, n):
                cnt3 += (m - arr[p].count('R'))
            
            if min_value > (cnt1+cnt2+cnt3):
                min_value = (cnt1+cnt2+cnt3)

    print(f'#{tc} {min_value}')