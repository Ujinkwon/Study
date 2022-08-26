import sys
sys.stdin = open('6190.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    res = -1
    for i in range(n):
        for j in range(i+1, n):
            num = str(arr[i] * arr[j])
            for k in range(1, len(num)):
                if num[k-1] > num[k]:
                    break
            else:
                if res < int(num):
                    res = int(num)

    print(f'#{tc} {res}')