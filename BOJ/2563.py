paper = [[0]*100 for _ in range(100)]
cnt = 0
t = int(input())
for _ in range(t):
    l, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(l, l+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                cnt += 1
print(cnt)
