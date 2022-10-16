import sys
sys.stdin = open('2920.txt')

nums = list(map(int, input().split()))
a = sorted(nums)
b = sorted(nums, reverse=True)
if nums == a:
    print('ascending')
elif nums == b:
    print('descending')
else:
    print('mixed')