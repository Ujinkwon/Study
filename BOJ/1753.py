import sys
from heapq import *
sys.stdin = open('1753.txt')

def dijkstra():
    while heap:
        w, v = heappop(heap)
        if d[v] < w:
            continue
        for w2, v2 in arr[v]:
            if d[v2] > w + w2:
                d[v2] = w + w2
                heappush(heap, (w+w2, v2))

v, e = map(int, input().split())
d = [10**8]*(v+1)
s = int(input())
arr = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))
d[s] = 0
heap = []
heappush(heap, (0, s))
dijkstra()
for i in range(1, len(d)):
    if d[i] == 10**8:
        d[i] = 'INF'
    print(d[i])