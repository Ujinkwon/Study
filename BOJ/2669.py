arr = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(4):
    xy = list(map(int, input().split()))
    for i in range(xy[1], xy[3]):
        for j in range(xy[0], xy[2]):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)
