from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = combinations_with_replacement(nums, m)
for i in arr:
    print(*i)