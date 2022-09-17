from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = permutations(nums, m)
for i in arr:
    print(*i)