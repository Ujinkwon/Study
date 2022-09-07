import sys
sys.stdin = open('2468.txt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_value, min_value = 0, 101
for i in range(n):
    if max_value < max(arr[i]):
        max_value = max(arr[i])
    if min_value > min(arr[i]):
        min_value = min(arr[i])

for i in range(min_value, max_value+1):
    print(i)