import sys
import copy
sys.stdin = open('14891.txt')

def move(n, d, arr):
    if d == 1:
        arr[n-1].insert(0, arr[n-1][-1])
        del arr[n-1][-1]
    elif d == -1:
        arr[n-1].append(arr[n-1][0])
        del arr[n-1][0]
    return arr

arr = [list(map(int, input())) for _ in range(4)]
k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    i = n
    dir = -d
    temp = copy.deepcopy(arr)
    if n == 1:
        while i < 4 and arr[i-1][2] != arr[i][6]:
            temp = move(i+1, dir, temp)
            i += 1
            dir = -dir
    elif n == 4:
        while i > 1 and arr[i-1][6] != arr[i-2][2]:
            temp = move(i, dir, temp)
            i -= 1
            dir = -dir
    elif n == 2:
        if arr[0][2] != arr[1][6]:
            temp = move(1, -d, temp)
        while i < 4 and arr[i-1][2] != arr[i][6]:
            temp = move(i+1, dir, temp)
            i += 1
            dir = -dir
    elif n == 3:
        if arr[2][2] != arr[3][6]:
            temp = move(4, -d, temp)
        while i > 1 and arr[i-1][6] != arr[i-2][2]:
            temp = move(i-1, dir, temp)
            i -= 1
            dir = -dir

    arr = move(n, d, temp)
res = 0
for i in range(4):
    res += (arr[i][0] * (2**i))
print(res)
