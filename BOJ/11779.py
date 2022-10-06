import sys
from heapq import *
sys.stdin = open('11779.txt')

def dijkstra(D, n):
    heap = []
    heappush(heap, (0, n))
    D[n] = 0
    while heap:
        w, node = heappop(heap)
        if D[node] < w:
            continue
        for e, w2 in adj[node]:
            cost = w2 + w
            if cost  < D[e]:
                D[e], arr[e] = cost, node
                heappush(heap, (cost, e))

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
start, end = map(int, input().split())
D = [1e9]*(n+1)
arr = [start]*(n+1)
dijkstra(D, start)

ans = []
temp = end
while temp != start:
    ans.append(str(temp))
    temp = arr[temp]
ans.append(str(start))
ans.reverse()

print(D[end])
print(len(ans))
print(*ans)