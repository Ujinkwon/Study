import sys
from heapq import *
sys.stdin = open('1197.txt')

v, e = map(int, input().split())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    n1, n2, w = map(int, input().split())
    arr[n1].append([w, n2])
    arr[n2].append([w, n1])
total = 0
MST = [1]
q = []
for i in arr[1]:
    heappush(q, i)
while len(MST) != v:
    w, n = heappop(q)
    if n in MST:
        continue
    MST.append(n)
    total += w
    for i in arr[n]:
        if i[1] not in MST:
            heappush(q, i)
print(total)

# MST = [1]
# q = [[], [(2, 1), (3, 3)]]
# pop = (2, 1)
#
# total = 1
# MST = [1, 2]
# q = [[], [(3, 3)], [(3, 2)]]
# pop = (3, 2)
#
# total = 1+2
# *stop
# 답은 3