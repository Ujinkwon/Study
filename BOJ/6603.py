import sys
from itertools import combinations
sys.stdin = open('6603.txt')

while 1:
    n = list(map(int, input().split()))
    if n[0] == 0:
        break
    nums = n[1:]
    arr = combinations(nums, 6)
    for i in arr:
        print(*i)
    print()