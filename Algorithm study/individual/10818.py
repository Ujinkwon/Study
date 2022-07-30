n = int(input())

nums = list(map(int, input().split()))
max_num = nums[0]
min_num = nums[0]

for num in nums:
    if max_num < num:
        max_num = num
    elif min_num > num:
        min_num = num

print(min_num, max_num)
