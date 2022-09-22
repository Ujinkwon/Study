import sys
sys.stdin = open('11501.txt')

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_value = arr[n-1]
    buy = []
    total = 0
    for i in range(n-2, -1, -1):
        if arr[i] < max_value:
            buy.append(arr[i])

        if arr[i] >= max_value or i == 0:
            for k in buy:
                total += (max_value-k)
            buy = []
            max_value = arr[i]
    print(total)