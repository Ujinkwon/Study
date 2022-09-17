from itertools import product
# 중복순열
n, m = map(int, input().split())
nums = list(range(1, n+1))
arr = product(nums, repeat=m)
for i in arr:
    print(*i)