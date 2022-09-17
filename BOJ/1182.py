from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, len(nums)+1):
    for j in list(combinations(nums, i)):
        if sum(j) == s:
            cnt += 1
print(cnt)