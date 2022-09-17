from itertools import combinations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = sorted(set(combinations(nums, m)))
for i in arr:
    print(*i)