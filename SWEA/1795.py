import sys
from heapq import *
sys.stdin = open('1795.txt')

def dijkstra(D, n):
    heap = []
    heappush(heap, (0, n))
    D[n] = 0
    while heap:
        distance, node = heappop(heap)
        if D[node] < distance:
            continue
        for i in adj[node]:
            if distance + i[1] < D[i[0]]:
                D[i[0]] = distance + i[1]
                heappush(heap, (D[i[0]], i[0]))

t = int(input())
for tc in range(1, t+1):
    n, m, x = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    D = [10**6]*(n+1)
    for _ in range(m):
        s, e, w = map(int, input().split())
        adj[s].append([e, w])
    dijkstra(D, x)
    go = D
    max_value = 0
    for i in range(1, n+1):
        if i != x:
            D = [10**6] * (n+1)
            dijkstra(D, i)
            if go[i] + D[x] > max_value:
                max_value = go[i] + D[x]
    print(f'#{tc} {max_value}')

# adj = [[], [(2, 4), (3, 2), (4, 7)], [(1, 1), (3, 5)], [(1, 2), (4, 4), (2, 3)]]
#
# 힙 : 거리, 도착노드
# heap = [ (0, 2) ]
# D = [ xx, xx, 0, xx, xx ]
# U = [ 2, ]
#
# 1) 거리, 도착노드 = heappop
# D에 들어가 있던 값이 작으면 pass
# 아니면
# 	인접노드 거리 기준으로 비교해서 작으면 덮고 push
#
# 0, 2
# 0 < 0 이므로
# 인접 노드 : (1, 1), (3, 5)
# (1) 1+0 < xx => D = [ xx, 1, 0, xx, xx ]
# 	        heap = [ (1, 1) ]
# (2) 5+0 < xx => D = [ xx, 1, 0, 5, xx ]
# 	        heap = [ (1, 1), (5, 3) ]
#
# 1, 1
# 1 < 1 이므로
# 인접 노드 : (2, 4), (3, 2), (4, 7)
# (1) 4+1 > 1
# (2) 2+1 < 5 => D = [ xx, 1, 0, 3, xx ]
# 	       heap = [ (5, 3), (3, 3) ]
# (3) 7+1 < xx => D = [ xx, 1, 0, 3, 8 ]
# 	        heap = [ (5, 3), (3, 3), (8, 4) ]