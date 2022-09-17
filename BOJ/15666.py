from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = sorted(set(combinations_with_replacement(nums, m)))
for i in arr:
    print(*i)