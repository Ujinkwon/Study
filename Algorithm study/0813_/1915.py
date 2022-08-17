n, m = map(int, input().split())
box = [list(map(int, input())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]
max_cnt = 0

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and box[i][j] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

            if dp[i][j] > max_cnt:
                max_cnt = dp[i][j]
                
print(max_cnt**2)
