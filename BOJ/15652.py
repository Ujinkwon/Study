from itertools import combinations_with_replacement
# 중복 조합
n, m = map(int, input().split())
nums = list(range(1, n+1))
arr = combinations_with_replacement(nums, m)
for i in arr:
    print(*i)