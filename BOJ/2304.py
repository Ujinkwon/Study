import sys
sys.stdin = open('2304.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_high = arr[0][1]
max_r = arr[0][0]
for i in arr:
    if max_high < i[1]:
        max_high = i[1]
    if max_r < i[0]:
        max_r = i[0]

home = [0]*(max_r + 1)
for i in arr:
    home[i[0]] = i[1]

num = 0
for i in range(home.index(max_high)):
    if num < home[i]:
        num = home[i]
    else: home[i] = num
num = 0
for i in range(len(home)-1, home.index(max_high), -1):
    if num < home[i]:
        num = home[i]
    else: home[i] = num

print(sum(home))