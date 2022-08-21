paper = [[0]*1001 for _ in range(1001)]
n = int(input())
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(arr[1], arr[1]+arr[3]):
        for k in range(arr[0], arr[0]+arr[2]):
            paper[j][k] = i

for k in range(n):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == k+1:
                cnt += 1
    print(cnt)
