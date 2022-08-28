import sys
sys.stdin = open('2564.txt')

r, c = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
d, x = map(int, input().split())
total = 0


for i in store:
    if d == 1:
        t = [1,2,3,c,r,i[1]]
    elif d == 2:
        t = [2,1,3,c,r,c-i[1]]
    elif d == 3:
        t = [3,4,1,r,c,i[1]]
    elif d == 4:
        t = [4,3,1,r,c,r-i[1]]

    if i[0] == t[0]:
        total += abs(x - i[1])
    elif i[0] == t[1]:
        total += abs(x - i[1]) + t[3]
        if i[1] > x:
            total += min(x, t[4]-i[1]) * 2
        else:
            total += min(t[4]-x, i[1]) * 2
    elif i[0] == t[2]:
        total += x + t[5]
    else:
        total += (t[4]-x) + t[5]

print(total)