import sys
from collections import deque
import time
sys.stdin = open('11003.txt')

start = time.time()
n, l = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()

for i in range(n):
    # i-L+1 인덱스 이전인 것들을 pop해준다.
    while q and q[0][0] <= i-l:
        q.popleft()

    # 들어갈 숫자보다 큰 것들은 전부 pop해준다.
    while q and q[-1][1] >= arr[i]:
        q.pop()

    q.append((i, arr[i]))
    print(q[0][1], end=' ')

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