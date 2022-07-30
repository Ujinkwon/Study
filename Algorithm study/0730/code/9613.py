
import sys
import math

t = int(input())

for i in range(t):
    arr = list(map(int, sys.stdin.readline().split()))
    total = 0
    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            total += math.gcd(arr[j], arr[k])

    print(total)