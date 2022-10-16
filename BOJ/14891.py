import sys
import copy
sys.stdin = open('14891.txt')

def move(n, d, arr):
    if d == 1:
        arr[n].insert(0, arr[n][-1])
        del arr[n][-1]
    elif d == -1:
        arr[n].append(arr[n][0])
        del arr[n][0]
    return arr

arr = [list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
    s, d = map(int, input().split())
    n = s-1
    dir = -d
    temp = copy.deepcopy(arr)
    if 0 <= n < 2:
        if n == 1:
            if arr[0][2] != arr[1][6]:
                temp = move(0, -d, temp)
        while n < 3 and arr[n][2] != arr[n+1][6]:
            temp = move(n+1, dir, temp)
            n += 1
            dir = -dir
    elif 1 < n < 4:
        if n == 2:
            if arr[2][2] != arr[3][6]:
                temp = move(3, -d, temp)
        while n > 0 and arr[n][6] != arr[n-1][2]:
            temp = move(n-1, dir, temp)
            n -= 1
            dir = -dir
    arr = move(s-1, d, temp)
res = 0
for i in range(4):
    res += (arr[i][0] * (2**i))
print(res)
