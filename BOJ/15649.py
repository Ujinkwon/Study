from itertools import permutations
# 순열
n, m = map(int, input().split())
nums = list(range(1, n+1))
res = permutations(nums, m)
for i in res:
    print(*i)