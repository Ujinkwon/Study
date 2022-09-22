import sys
sys.stdin = open('2457.txt')

n = int(input())
arr = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    arr.append([a*100+b, c*100+d])
arr.sort()
e = 0
for i in range(n):
    if arr[i][0] <= 301 and arr[i][1] > e:
        e = arr[i][1]
        idx = i
print(idx)
print(arr)