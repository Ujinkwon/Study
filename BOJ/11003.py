import sys
from collections import deque
import time
sys.stdin = open('11003.txt')

start = time.time()
n, l = map(int, input().split())
arr = list(map(int, input().split()))


# res = []
# for i in range(1, n+1):
#     s = i-l
#     if i-l < 0:
#         s = 0
#     res.append(min(arr[s:i]))
# print(*res)
# print('time :', time.time() - start)


# res = [arr[0], min(arr[0], arr[1])]
# left, right = 0, l-1
# total = arr[left:right+1]
#
# while right < n:
#     res.append(min(arr[left:right+1]))
#     left += 1
#     right += 1
# print(*res)