import sys
from heapq import *
sys.stdin = open('1238.txt')

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
print(max_value)