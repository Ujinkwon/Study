import sys
sys.stdin = open('2116.txt')

n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
fix = {0 : 5, 1 : 3, 2 : 4, 4 : 2, 3 : 1, 5 : 0}
result = []

for i in range(6):
    arr = []
    arr.append([dice[0][i], dice[0][fix[i]]])
    m = dice[0][fix[i]]

    for j in range(1, n):
        m = dice[j].index(m)
        arr.append([dice[j][m], dice[j][fix[m]]])
        m = dice[j][fix[m]]

    total = 0
    for k in range(n):
        num = [1, 2, 3, 4, 5, 6]
        for l in arr[k]:
            num.remove(l)
        total += max(num)
    result.append(total)
print(max(result))
    

