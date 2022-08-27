import sys
sys.stdin = open('2477.txt')

k = int(input())
xmax, ymax = 0, 0
num, dir = [], []
for i in range(6):
    d, n = map(int, input().split())
    if d == 1 or d == 2:
        if xmax < n:
            xmax = n
    elif d == 3 or d == 4:
        if ymax < n:
            ymax = n
    num.append(n)
    dir.append(d)
minbox = 1
for i in range(6):
    two, three = i-2, i-3
    if two < -1:
        two += 6
    if three < -1:
        three += 6
    if dir[three] ==dir[i-1] and dir[two] == dir[i]:
        minbox = num[i-1] * num[i-2]
        break

print(k * ((xmax*ymax)-minbox))
