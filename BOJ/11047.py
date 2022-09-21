import sys
sys.stdin = open('11047.txt')

n, k = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    if a <= k:
        arr.append(a)

total = 0
for i in arr[::-1]:
    total += (k // i)
    k = k % i
print(total)