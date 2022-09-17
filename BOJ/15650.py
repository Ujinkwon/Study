from itertools import combinations
# 조합
n, m = map(int, input().split())
nums = list(range(1, n+1))
res = combinations(nums, m)
for i in res:
    print(*i)
