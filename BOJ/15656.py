from itertools import product

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = product(nums, repeat=m)
for i in arr:
    print(*i)