from itertools import product

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = sorted(set(product(nums, repeat=m)))
for i in arr:
    print(*i)