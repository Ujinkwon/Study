import sys
sys.stdin = open('2170.txt')


n = int(input())
arr = list(map(int, input().split()))
for _ in range(n-1):
    x, y = map(int, input().split())
    for i in range(len(arr)):
        if arr[i][0] %