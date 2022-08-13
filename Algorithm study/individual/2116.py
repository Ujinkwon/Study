n = int(input())
dice = [list(map(int, input())) for _ in range(n)]
fix = {0 : 5, 1 : 3, 2 : 4, 4 : 2, 3 : 1, 5 : 0}
print(fix[2])

for i in range(n):
    for j in range(6):
        dice[i][j]
        dice[i][fix[j]]
        dice[i+1][fix]